"""Parameters for the prisoner's dilemma."""

from __future__ import annotations

rounds_to_play: int = 20

punishment_years: dict[str, int] = {
    "both_cooperate": 1,
    "both_defect": 4,
    "win": 0,
    "loose": 10,
}
