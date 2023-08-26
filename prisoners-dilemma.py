"""Simple simulation of the prisoner's dilemma experiment.

Inspired by Axelrod's "Evolution of Cooperation" (1984).
"""

from __future__ import annotations

import random
import sys


def color_print(color: str, text: str) -> None:
    """Print colored text with ANSI escape codes for the terminal."""
    colors = {
        "blue": "\033[1;34m",  # ] -- needed to fix confusing the indentationexpr
        "green": "\033[1;32m",  # ]
        "yellow": "\033[1;33m",  # ]
        "red": "\033[1;31m",  # ]
        "reset": "\033[0m",  # ]
    }
    print(colors[color] + text + colors["reset"])


# ──────────────────────────────────────────────────────────────────────────────


available_strats = ["always_cooperate", "always_defect", "random", "alternate", "revenge"]


def strategy_to_action(actor_self: str, strategy: str, previous_runs: list[dict[str, str]]) -> str:
    """Given a strategy, return an action, either "cooperate" or "defect".

    Available strategies are:
        - always_cooperate
        - always_defect
        - random
        - alternate: alternate between cooperation and defection
        - revenge: if opponent defected last round, defect, otherwise cooperate
    """
    opponent = "actor2" if actor_self == "actor1" else "actor1"

    if strategy == "always_cooperate":
        return "cooperate"
    if strategy == "always_defect":
        return "defect"
    if strategy == "random":
        return random.choice(["cooperate", "defect"])
    if strategy == "alternate":
        return "cooperate" if previous_runs[-1][actor_self] == "defect" else "defect"
    if strategy == "revenge":
        last_opponent_action = previous_runs[-1][opponent]
        return "defect" if last_opponent_action == "defect" else "cooperate"
    return ""


def play_game(actor1_strategy: str, actor2_strategy: str, rounds: int) -> dict[str, int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds."""
    outcome = {"actor1": 0, "actor2": 0}
    previous_runs = []

    for _ in range(rounds):
        actor1_action = strategy_to_action("actor1", actor1_strategy, previous_runs)
        actor2_action = strategy_to_action("actor2", actor2_strategy, previous_runs)
        if actor1_action == "cooperate" and actor2_action == "cooperate":
            outcome["actor1"] += 1
            outcome["actor2"] += 1
        elif actor1_action == "defect" and actor2_action == "defect":
            outcome["actor1"] += 2
            outcome["actor2"] += 2
        elif actor1_action == "cooperate" and actor2_action == "defect":
            outcome["actor1"] += 3
            outcome["actor2"] += 0
        elif actor1_action == "defect" and actor2_action == "cooperate":
            outcome["actor1"] += 0
            outcome["actor2"] += 3
        previous_runs.append({"actor1": actor1_action, "actor2": actor2_action})

    return outcome


def main() -> None:
    """Execute main function."""
    # read & validate input
    parameters_needed = 3
    if len(sys.argv) < parameters_needed + 1:  # +1, as argv[0] is script name
        color_print(
            "yellow",
            "Usage: prisoners-dilemma.py <rounds> <actor1_strategy> <actor2_strategy>",
        )
        return

    rounds = int(sys.argv[1])
    actor1_strat = sys.argv[2]
    actor2_strat = sys.argv[3]
    if actor1_strat not in available_strats or actor2_strat not in available_strats:
        color_print(
            "yellow", "Invalid strategy. Available strategies:" + ", ".join(available_strats),
        )
        return

    # play the game
    outcome = play_game(actor1_strat, actor2_strat, rounds)

    # output
    color_print("green", "Prisoners' Dilemma")
    color_print("green", "──────────────────")

    color_print("blue", "Strategies used:")
    print("Actor 1:", actor1_strat)
    print("Actor 2:", actor2_strat)
    print()

    color_print("blue", "Rounds:")
    print(rounds)
    print()

    color_print("blue", "Outcome:")
    print(f"Actor 1: {outcome['actor1']} years")
    print(f"Actor 2: {outcome['actor2']} years")


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
