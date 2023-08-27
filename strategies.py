"""Implementation of the Strategies for the Prisoners' Dilemma."""

from __future__ import annotations

import random

# ──────────────────────────────────────────────────────────────────────────────


def __opponent_past_actions(
    self_id: int,
    prev_runs: list[tuple[str, str]],
) -> list[str]:
    """Create a list of the opponents last actions."""
    opponent_id = 1 if self_id == 0 else 0
    past_opponent_actions = (run[opponent_id] for run in prev_runs)
    return list(past_opponent_actions)


def __is_first_run(prev_runs: list[tuple[str, str]]) -> bool:
    return len(prev_runs) == 0


# ──────────────────────────────────────────────────────────────────────────────


def alternate(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """Alternate between cooperating and defecting."""
    if __is_first_run(prev_runs):
        return "cooperate"
    last_own_action = prev_runs[-1][self_id]
    return "defect" if last_own_action == "cooperate" else "cooperate"


def tit_for_tat(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """Mirrors last action taken by the opponent."""
    if __is_first_run(prev_runs):
        return "cooperate"
    last_opponent_action = __opponent_past_actions(self_id, prev_runs)[-1]
    return last_opponent_action


def unforgiving(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """If the opponent has defected at any time in the past, defect."""
    if __is_first_run(prev_runs):
        return "cooperate"
    opponent_has_defected_once = "defect" in __opponent_past_actions(self_id, prev_runs)
    return "defect" if opponent_has_defected_once else "cooperate"


def opportunist(self_id: int, prev_runs: list[tuple[str, str]]) -> str:
    """Defect if the opponent has always cooperated recently."""
    min_runs = 2  # number of runs considered as "recently"
    is_first_few_runs = len(prev_runs) > min_runs
    if is_first_few_runs:
        return "cooperate"
    last_few_runs_opp_actions = __opponent_past_actions(self_id, prev_runs)[-min_runs:]
    opp_cooperated_recently = "defect" not in last_few_runs_opp_actions
    return "defect" if opp_cooperated_recently else "cooperate"


strategy_funcs = {
    "always_cooperate": lambda *_: "cooperate",
    "always_defect": lambda *_: "defect",
    "random": lambda *_: random.choice(["cooperate", "defect"]),
    "alternate": alternate,
    "tit_for_tat": tit_for_tat,
    "unforgiving": unforgiving,
    "opportunist": opportunist,
}


def describe_all_strategies() -> str:
    """Describe all available strategies."""
    out = ""
    for name, strategy_func in strategy_funcs.items():
        desc = strategy_func.__doc__
        if desc is None:
            out += f"- {name}\n"
        else:
            out += f"- {name}: {strategy_func.__doc__}\n"
    return out
