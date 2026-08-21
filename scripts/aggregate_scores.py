#!/usr/bin/env python3
"""Aggregate anonymous CS PhD SOP rubric scores deterministically.

The script accepts only anonymous document/judge identifiers, gate status,
integer D1-D7 ratings, and optional pairwise outcomes. It never needs or
retains SOP text.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
from pathlib import Path
from typing import Any, Iterable


WEIGHTS = {
    "D1": 15,
    "D2": 20,
    "D3": 15,
    "D4": 15,
    "D5": 10,
    "D6": 15,
    "D7": 10,
}
CORE_DIMENSIONS = ("D1", "D2", "D3", "D4", "D5", "D7")
CORE_MAXIMUM = sum(WEIGHTS[dimension] for dimension in CORE_DIMENSIONS)
ALLOWED_MODES = {"same_program", "cross_program"}
ALLOWED_GATE_STATUSES = {"PASS", "REVISE", "BLOCKED", "UNVERIFIED"}
ALLOWED_PAIRWISE_OUTCOMES = {"TIE", "INSUFFICIENT_EVIDENCE"}
ID_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{1,63}$")
SLUG_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{1,95}$")
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
PHONE_PATTERN = re.compile(r"(?<!\w)(?:\+?\d[\d ().-]{7,}\d)(?!\w)")
LOCAL_PATH_PATTERN = re.compile(r"(?:/(?:Users|home)/|[A-Za-z]:\\\\Users\\\\)")
SENSITIVE_KEY_PARTS = {
    "address",
    "applicant",
    "birth",
    "contact",
    "cv",
    "email",
    "essay",
    "full_name",
    "legal_name",
    "name",
    "phone",
    "student_id",
    "sop_text",
    "text",
}


class ValidationError(ValueError):
    """Raised for malformed or unsafe aggregation input."""


def _round(value: float) -> float:
    return round(value + 0.0, 2)


def _median(values: Iterable[float]) -> float:
    materialized = list(values)
    if not materialized:
        raise ValidationError("Cannot compute a median from an empty score list.")
    return float(statistics.median(materialized))


def _weighted_full_score(judge: dict[str, Any]) -> float:
    return sum(judge[dimension] / 4 * weight for dimension, weight in WEIGHTS.items())


def _normalized_core_score(judge: dict[str, Any]) -> float:
    weighted_core = sum(
        judge[dimension] / 4 * WEIGHTS[dimension] for dimension in CORE_DIMENSIONS
    )
    return weighted_core / CORE_MAXIMUM * 100


def _local_fit_score(judge: dict[str, Any]) -> float:
    return judge["D6"] / 4 * 100


def _path(parent: str, child: str) -> str:
    return f"{parent}.{child}" if parent else child


def _scan_privacy(value: Any, location: str = "input") -> list[str]:
    """Return warnings without copying sensitive values into output."""
    warnings: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            key_text = str(key)
            item_path = _path(location, key_text)
            normalized = key_text.lower().replace("-", "_").replace(" ", "_")
            if normalized in SENSITIVE_KEY_PARTS or any(
                normalized.endswith(f"_{part}") for part in SENSITIVE_KEY_PARTS
            ):
                warnings.append(f"Potential personal or document-content field at {item_path}.")
            warnings.extend(_scan_privacy(item, item_path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            warnings.extend(_scan_privacy(item, f"{location}[{index}]"))
    elif isinstance(value, str):
        if EMAIL_PATTERN.search(value):
            warnings.append(f"Possible email address at {location}.")
        if PHONE_PATTERN.search(value):
            warnings.append(f"Possible phone number at {location}.")
        if LOCAL_PATH_PATTERN.search(value):
            warnings.append(f"Possible local filesystem path at {location}.")
    return list(dict.fromkeys(warnings))


def _warn_unknown_keys(
    record: dict[str, Any], allowed: set[str], location: str
) -> list[str]:
    return [
        f"Unsupported field ignored at {_path(location, str(key))}."
        for key in record
        if key not in allowed
    ]


def _require_mapping(value: Any, location: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{location} must be a JSON object.")
    return value


def _require_list(value: Any, location: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValidationError(f"{location} must be a JSON array.")
    return value


def _validate_id(value: Any, location: str) -> str:
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise ValidationError(
            f"{location} must be an anonymous 2-64 character ID using letters, "
            "numbers, dots, underscores, or hyphens (for example, SOP-A01)."
        )
    return value


def _validate_dimension_score(value: Any, location: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 4:
        raise ValidationError(f"{location} must be an integer from 0 to 4.")
    return value


def _validate_threshold(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValidationError("near_score_threshold must be a number from 0 to 100.")
    threshold = float(value)
    if not math.isfinite(threshold) or not 0 <= threshold <= 100:
        raise ValidationError("near_score_threshold must be a finite number from 0 to 100.")
    return threshold


def validate_input(data: Any, strict_privacy: bool = False) -> tuple[dict[str, Any], list[str]]:
    """Validate input and return a minimal normalized record plus warnings."""
    root = _require_mapping(data, "input")
    warnings = _scan_privacy(root)
    warnings.extend(
        _warn_unknown_keys(root, {"mode", "near_score_threshold", "sops", "pairwise"}, "input")
    )

    mode = root.get("mode")
    if mode not in ALLOWED_MODES:
        raise ValidationError("mode must be same_program or cross_program.")
    threshold = _validate_threshold(root.get("near_score_threshold", 5.0))

    raw_sops = _require_list(root.get("sops"), "sops")
    if not raw_sops:
        raise ValidationError("sops must contain at least one scored document.")

    normalized_sops: list[dict[str, Any]] = []
    sop_ids: set[str] = set()
    for sop_index, raw_sop in enumerate(raw_sops):
        sop_location = f"sops[{sop_index}]"
        sop = _require_mapping(raw_sop, sop_location)
        warnings.extend(
            _warn_unknown_keys(sop, {"sop_id", "gate_status", "judges"}, sop_location)
        )
        sop_id = _validate_id(sop.get("sop_id"), f"{sop_location}.sop_id")
        if sop_id in sop_ids:
            raise ValidationError(f"Duplicate sop_id: {sop_id}.")
        sop_ids.add(sop_id)

        gate_status = sop.get("gate_status")
        if gate_status not in ALLOWED_GATE_STATUSES:
            raise ValidationError(
                f"{sop_location}.gate_status must be PASS, REVISE, BLOCKED, or UNVERIFIED."
            )

        raw_judges = _require_list(sop.get("judges"), f"{sop_location}.judges")
        if not raw_judges:
            raise ValidationError(f"{sop_location}.judges must contain at least one judge.")
        normalized_judges: list[dict[str, Any]] = []
        judge_ids: set[str] = set()
        for judge_index, raw_judge in enumerate(raw_judges):
            judge_location = f"{sop_location}.judges[{judge_index}]"
            judge = _require_mapping(raw_judge, judge_location)
            warnings.extend(
                _warn_unknown_keys(judge, {"judge_id", *WEIGHTS}, judge_location)
            )
            judge_id = _validate_id(judge.get("judge_id"), f"{judge_location}.judge_id")
            if judge_id in judge_ids:
                raise ValidationError(f"Duplicate judge_id {judge_id} for {sop_id}.")
            judge_ids.add(judge_id)
            normalized_judge: dict[str, Any] = {"judge_id": judge_id}
            for dimension in WEIGHTS:
                normalized_judge[dimension] = _validate_dimension_score(
                    judge.get(dimension), f"{judge_location}.{dimension}"
                )
            normalized_judges.append(normalized_judge)

        normalized_sops.append(
            {
                "sop_id": sop_id,
                "gate_status": gate_status,
                "judges": normalized_judges,
            }
        )

    raw_pairwise = _require_list(root.get("pairwise", []), "pairwise")
    normalized_pairwise: list[dict[str, str]] = []
    for pair_index, raw_pair in enumerate(raw_pairwise):
        pair_location = f"pairwise[{pair_index}]"
        pair = _require_mapping(raw_pair, pair_location)
        warnings.extend(
            _warn_unknown_keys(
                pair, {"a", "b", "winner", "judge_id", "dimension"}, pair_location
            )
        )
        a = _validate_id(pair.get("a"), f"{pair_location}.a")
        b = _validate_id(pair.get("b"), f"{pair_location}.b")
        if a == b:
            raise ValidationError(f"{pair_location} must compare two different SOP IDs.")
        if a not in sop_ids or b not in sop_ids:
            raise ValidationError(f"{pair_location} references an unknown SOP ID.")
        winner = pair.get("winner")
        if winner not in {a, b, *ALLOWED_PAIRWISE_OUTCOMES}:
            raise ValidationError(
                f"{pair_location}.winner must be {a}, {b}, TIE, or INSUFFICIENT_EVIDENCE."
            )
        judge_id = _validate_id(pair.get("judge_id"), f"{pair_location}.judge_id")
        dimension = pair.get("dimension")
        if not isinstance(dimension, str) or not SLUG_PATTERN.fullmatch(dimension):
            raise ValidationError(
                f"{pair_location}.dimension must be a short non-personal slug."
            )
        normalized_pairwise.append(
            {
                "a": a,
                "b": b,
                "winner": winner,
                "judge_id": judge_id,
                "dimension": dimension,
            }
        )

    warnings = list(dict.fromkeys(warnings))
    if strict_privacy and warnings:
        raise ValidationError(
            "Strict privacy validation failed: " + " ".join(warnings)
        )

    return (
        {
            "mode": mode,
            "near_score_threshold": threshold,
            "sops": normalized_sops,
            "pairwise": normalized_pairwise,
        },
        warnings,
    )


def _score_record(sop: dict[str, Any]) -> dict[str, Any]:
    judges = sop["judges"]
    full_scores = [_weighted_full_score(judge) for judge in judges]
    core_scores = [_normalized_core_score(judge) for judge in judges]
    local_fit_scores = [_local_fit_score(judge) for judge in judges]
    disagreements = {
        dimension: max(judge[dimension] for judge in judges)
        - min(judge[dimension] for judge in judges)
        for dimension in WEIGHTS
    }
    return {
        "sop_id": sop["sop_id"],
        "rankable": sop["gate_status"] != "BLOCKED",
        "gate_status": sop["gate_status"],
        "median_full_score": _round(_median(full_scores)),
        "median_core_score": _round(_median(core_scores)),
        "median_local_fit_score": _round(_median(local_fit_scores)),
        "judge_full_score_range": [_round(min(full_scores)), _round(max(full_scores))],
        "judge_core_score_range": [_round(min(core_scores)), _round(max(core_scores))],
        "max_dimension_disagreement": max(disagreements.values()),
        "adjudication_dimensions": [
            dimension for dimension, difference in disagreements.items() if difference >= 2
        ],
        "pairwise_points": 0.0,
        "pairwise_comparisons": 0,
        "pairwise_record": {"wins": 0, "ties": 0, "losses": 0, "insufficient": 0},
        "tier": "",
    }


def _apply_pairwise(results_by_id: dict[str, dict[str, Any]], pairwise: list[dict[str, str]]) -> None:
    for comparison in pairwise:
        a = results_by_id[comparison["a"]]
        b = results_by_id[comparison["b"]]
        winner = comparison["winner"]
        if winner == "INSUFFICIENT_EVIDENCE":
            a["pairwise_record"]["insufficient"] += 1
            b["pairwise_record"]["insufficient"] += 1
            continue
        a["pairwise_comparisons"] += 1
        b["pairwise_comparisons"] += 1
        if winner == "TIE":
            a["pairwise_points"] += 0.5
            b["pairwise_points"] += 0.5
            a["pairwise_record"]["ties"] += 1
            b["pairwise_record"]["ties"] += 1
        elif winner == comparison["a"]:
            a["pairwise_points"] += 1.0
            a["pairwise_record"]["wins"] += 1
            b["pairwise_record"]["losses"] += 1
        else:
            b["pairwise_points"] += 1.0
            b["pairwise_record"]["wins"] += 1
            a["pairwise_record"]["losses"] += 1


def _ranking_score(result: dict[str, Any], mode: str) -> float:
    return (
        result["median_full_score"]
        if mode == "same_program"
        else result["median_core_score"]
    )


def _ranking_range(result: dict[str, Any], mode: str) -> list[float]:
    return (
        result["judge_full_score_range"]
        if mode == "same_program"
        else result["judge_core_score_range"]
    )


def _assign_tiers(results: list[dict[str, Any]], mode: str, threshold: float) -> None:
    pass_results = sorted(
        (result for result in results if result["gate_status"] == "PASS"),
        key=lambda result: (-_ranking_score(result, mode), result["sop_id"]),
    )
    tier_number = 0
    previous_score: float | None = None
    for result in pass_results:
        score = _ranking_score(result, mode)
        if previous_score is None or previous_score - score > threshold:
            tier_number += 1
        result["tier"] = f"Tier {tier_number}"
        previous_score = score

    for result in results:
        if result["gate_status"] in {"REVISE", "UNVERIFIED"}:
            result["tier"] = "Provisional"
        elif result["gate_status"] == "BLOCKED":
            result["tier"] = "Blocked"


def _near_score_pairs(
    results: list[dict[str, Any]],
    pairwise: list[dict[str, str]],
    mode: str,
    threshold: float,
) -> list[dict[str, Any]]:
    eligible = sorted(
        (result for result in results if result["rankable"]),
        key=lambda result: result["sop_id"],
    )
    output: list[dict[str, Any]] = []
    for left_index, left in enumerate(eligible):
        for right in eligible[left_index + 1 :]:
            gap = abs(_ranking_score(left, mode) - _ranking_score(right, mode))
            left_range = _ranking_range(left, mode)
            right_range = _ranking_range(right, mode)
            ranges_overlap = max(left_range[0], right_range[0]) <= min(
                left_range[1], right_range[1]
            )
            if gap > threshold and not ranges_overlap:
                continue
            reviews = [
                {
                    "winner": item["winner"],
                    "judge_id": item["judge_id"],
                    "dimension": item["dimension"],
                }
                for item in pairwise
                if {item["a"], item["b"]} == {left["sop_id"], right["sop_id"]}
            ]
            output.append(
                {
                    "a": left["sop_id"],
                    "b": right["sop_id"],
                    "score_gap": _round(gap),
                    "judge_ranges_overlap": ranges_overlap,
                    "pairwise_review_required": not reviews,
                    "pairwise_reviews": reviews,
                }
            )
    return output


def aggregate(data: Any, strict_privacy: bool = False) -> dict[str, Any]:
    normalized, privacy_warnings = validate_input(data, strict_privacy=strict_privacy)
    mode = normalized["mode"]
    threshold = normalized["near_score_threshold"]
    results = [_score_record(sop) for sop in normalized["sops"]]
    results_by_id = {result["sop_id"]: result for result in results}
    _apply_pairwise(results_by_id, normalized["pairwise"])
    _assign_tiers(results, mode, threshold)

    status_order = {"PASS": 0, "REVISE": 1, "UNVERIFIED": 1, "BLOCKED": 2}
    results.sort(
        key=lambda result: (
            status_order[result["gate_status"]],
            -_ranking_score(result, mode),
            result["sop_id"],
        )
    )
    for result in results:
        result["pairwise_points"] = _round(result["pairwise_points"])
        result["ranking_score"] = _ranking_score(result, mode)
        result["judge_ranking_score_range"] = _ranking_range(result, mode)

    limitations = [
        "Scores and tiers describe SOP document quality, not applicant quality or admission probability.",
        "Tiers are provisional clusters; close or overlapping scores require evidence-based pairwise review.",
    ]
    if mode == "cross_program":
        limitations.append(
            "Cross-program ranking excludes D6; local fit is reported separately and is not a ranking input."
        )

    return {
        "mode": mode,
        "ranking_basis": "full_score" if mode == "same_program" else "normalized_core_score",
        "weights": WEIGHTS,
        "near_score_threshold": threshold,
        "results": results,
        "near_score_pairs": _near_score_pairs(
            results, normalized["pairwise"], mode, threshold
        ),
        "privacy_warnings": privacy_warnings,
        "limitations": limitations,
    }


def _self_test() -> None:
    sample = {
        "mode": "cross_program",
        "near_score_threshold": 5,
        "sops": [
            {
                "sop_id": "SOP-A01",
                "gate_status": "PASS",
                "judges": [
                    {
                        "judge_id": "J-1",
                        "D1": 3,
                        "D2": 4,
                        "D3": 3,
                        "D4": 3,
                        "D5": 3,
                        "D6": 1,
                        "D7": 3,
                    },
                    {
                        "judge_id": "J-2",
                        "D1": 3,
                        "D2": 3,
                        "D3": 3,
                        "D4": 3,
                        "D5": 3,
                        "D6": 1,
                        "D7": 4,
                    },
                ],
            },
            {
                "sop_id": "SOP-B01",
                "gate_status": "PASS",
                "judges": [
                    {
                        "judge_id": "J-1",
                        "D1": 3,
                        "D2": 3,
                        "D3": 3,
                        "D4": 3,
                        "D5": 3,
                        "D6": 4,
                        "D7": 3,
                    },
                    {
                        "judge_id": "J-2",
                        "D1": 3,
                        "D2": 3,
                        "D3": 3,
                        "D4": 3,
                        "D5": 3,
                        "D6": 4,
                        "D7": 3,
                    },
                ],
            },
        ],
        "pairwise": [],
    }
    output = aggregate(sample, strict_privacy=True)
    assert output["ranking_basis"] == "normalized_core_score"
    assert output["results"][0]["sop_id"] == "SOP-A01"
    assert output["results"][0]["median_local_fit_score"] == 25.0
    assert output["results"][1]["median_local_fit_score"] == 100.0
    assert output["near_score_pairs"]

    blocked = json.loads(json.dumps(sample))
    blocked["sops"][0]["gate_status"] = "BLOCKED"
    blocked_output = aggregate(blocked)
    blocked_result = next(
        item for item in blocked_output["results"] if item["sop_id"] == "SOP-A01"
    )
    assert blocked_result["rankable"] is False
    assert blocked_result["tier"] == "Blocked"

    private = json.loads(json.dumps(sample))
    private["sops"][0]["name"] = "Example Person"
    assert aggregate(private)["privacy_warnings"]
    try:
        aggregate(private, strict_privacy=True)
    except ValidationError:
        pass
    else:
        raise AssertionError("Strict privacy mode should reject personal fields.")


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aggregate anonymous D1-D7 CS PhD SOP evaluation scores."
    )
    parser.add_argument("input", nargs="?", help="Input JSON file. Reads stdin when omitted.")
    parser.add_argument("--output", help="Optional output JSON file; defaults to stdout.")
    parser.add_argument(
        "--strict-privacy",
        action="store_true",
        help="Fail if unsupported, personal, document-text, or local-path fields are detected.",
    )
    parser.add_argument(
        "--self-test", action="store_true", help="Run built-in deterministic checks and exit."
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        _self_test()
        print("Self-test passed.")
        return 0

    try:
        if args.input:
            data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        else:
            data = json.load(sys.stdin)
        output = aggregate(data, strict_privacy=args.strict_privacy)
        rendered = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, json.JSONDecodeError, ValidationError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
