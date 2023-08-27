"""Implementation of the Strategies for the Prisoners' Dilemma."""

from __future__ import annotations

import random

# ──────────────────────────────────────────────────────────────────────────────


def strat_alternate(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """Alternate between cooperating and defecting."""
    is_first_run = len(prev_runs) == 0
    if is_first_run:
        return "cooperate"
    last_self_action = prev_runs[-1][self_id]
    return "defect" if last_self_action == "cooperate" else "cooperate"

def strat_tit_for_tat(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """Mirrors last action taken by the opponent."""
    is_first_run = len(prev_runs) == 0
    if is_first_run:
        return "cooperate"
    opponent_id = 1 if self_id == 0 else 0
    last_opponent_action = prev_runs[-1][opponent_id]
    return last_opponent_action

def strat_unforgiving(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """If the opponent has defected at any time in the past, defect."""
    is_first_run = len(prev_runs) == 0
    if is_first_run:
        return "cooperate"
    opponent_id = 1 if self_id == 0 else 0
    prev_opponnent_actions = (run[opponent_id] for run in prev_runs)
    opponent_has_defected_once = "defect" in prev_opponnent_actions
    return "defect" if opponent_has_defected_once else "cooperate"

strategy_funcs = {
    "always_cooperate": lambda *_: "cooperate",
    "always_defect": lambda *_: "defect",
    "random": lambda *_: random.choice(["cooperate", "defect"]),
    "alternate": strat_alternate,
    "tit-for-tat": strat_tit_for_tat,
    "unforgiving": strat_unforgiving,
}

