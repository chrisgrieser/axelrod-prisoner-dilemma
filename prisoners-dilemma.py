"""Simple simulation of the prisoner's dilemma experiment.

Inspired by Axelrod's "Evolution of Cooperation" (1984).
"""

from __future__ import annotations

import random
import sys

# ──────────────────────────────────────────────────────────────────────────────


def colored_print(color: str, text: str) -> None:
    """Print colored text."""
    colors = {
        "blue": "\033[1;34m",  # ] -- needed to fix confusing the indentationexpr
        "green": "\033[1;32m",  # ]
        "yellow": "\033[1;33m",  # ]
        "red": "\033[1;31m",  # ]
        "reset": "\033[0m",  # ]
    }
    print(colors[color] + text + colors["reset"])


def strategy_to_action(strategy: str) -> str:
    """Given a strategy, return an action, either "cooperate" or "defect"."""
    if strategy == "always_cooperate":
        return "cooperate"
    if strategy == "always_defect":
        return "defect"
    if strategy == "random":
        return random.choice(["cooperate", "defect"])
    return ""


def play_game(actor1_strategy: str, actor2_strategy: str, rounds: int) -> dict[str, int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds."""
    outcome = {"actor1": 0, "actor2": 0}

    for _ in range(rounds):
        actor1_action = strategy_to_action(actor1_strategy)
        actor2_action = strategy_to_action(actor2_strategy)
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
    return outcome


def main() -> None:
    """Execute main function."""
    # read rounds from stdin, default: 1 round
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    # play the game
    actor1_strategy = "always_defect"
    actor2_strategy = "always_cooperate"
    outcome = play_game(actor1_strategy, actor2_strategy, rounds)

    # output
    colored_print("green", "Prisoners' Dilemma")
    colored_print("green", "──────────────────")

    colored_print("blue", "Strategies used:")
    print("Actor 1:", actor1_strategy)
    print("Actor 2:", actor2_strategy)
    print()

    colored_print("blue", "Rounds:")
    print(rounds)
    print()

    colored_print("blue", "Outcome:")
    print(f"Actor 1: {outcome['actor1']} years")
    print(f"Actor 2: {outcome['actor2']} years")


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
