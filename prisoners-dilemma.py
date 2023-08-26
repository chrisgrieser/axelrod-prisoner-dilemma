"""Simple simulation of the prisoner's dilemma experiment.

Inspired by Axelrod's "Evolution of Cooperation" (1984).
Prior software: https://github.com/Axelrod-Python/Axelrod
"""

from __future__ import annotations

import random
import sys

# ──────────────────────────────────────────────────────────────────────────────


def color_print(color: str, text: str) -> None:
    """Print colored text with ANSI escape codes for the terminal."""
    colors = {
        "magenta": "\033[1;35m",  # ] -- needed to fix confusing the indentationexpr
        "blue": "\033[1;34m",  # ]
        "green": "\033[1;32m",  # ]
        "yellow": "\033[1;33m",  # ]
        "red": "\033[1;31m",  # ]
        "reset": "\033[0m",  # ]
    }
    print(colors[color] + text + colors["reset"])


# ──────────────────────────────────────────────────────────────────────────────

available_strats = ["always_cooperate", "always_defect", "random", "alternate", "tit-for-tat"]


def strategy_to_action(
    actor_self: str,
    strategy: str,
    previous_runs: list[dict[str, str]],
) -> str:
    """Given the actors idendity, their strategy, and the previous rounds.

    Possible actions are:
        - cooperate
        - defect

    Available strategies are:
        - always_cooperate
        - always_defect
        - random
        - alternate: alternate between cooperation and defection
        - tit-for-tat: begin with cooperation, and copy the opponent's last action
    """
    opponent = "actor2" if actor_self == "actor1" else "actor1"
    is_first_run = len(previous_runs) == 0
    action = ""

    if strategy == "always_cooperate":
        action = "cooperate"
    elif strategy == "always_defect":
        action = "defect"
    elif strategy == "random":
        action = random.choice(["cooperate", "defect"])
    elif strategy == "alternate":
        if is_first_run:
            action = "cooperate"
        else:
            last_self_action = previous_runs[-1][actor_self]
            action = "defect" if last_self_action == "cooperate" else "cooperate"
    elif strategy == "tit-for-tat":
        if is_first_run:
            action = "cooperate"
        else:
            last_opponent_action = previous_runs[-1][opponent]
            action = last_opponent_action

    return action


def play_game(actor1_strat: str, actor2_strat: str, rounds: int) -> dict[str, int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds."""
    outcome = {"actor1": 0, "actor2": 0}
    run_history = []  # keep track of previous rounds, i.e. a memory for the actors

    for _ in range(rounds):
        actor1_action = strategy_to_action("actor1", actor1_strat, run_history)
        actor2_action = strategy_to_action("actor2", actor2_strat, run_history)
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
        run_history.append({"actor1": actor1_action, "actor2": actor2_action})

    return outcome


def main() -> None:
    """Execute main function.

    Usage: python3 prisoners-dilemma.py <rounds> <actor1_strategy> <actor2_strategy>
    """
    # read & validate input
    parameters_needed = 3
    if len(sys.argv) < parameters_needed + 1:  # +1, as argv[0] is script name
        color_print("yellow", "Expected parameters: <rounds> <actor1_strategy> <actor2_strategy>")
        return

    try:
        rounds = int(sys.argv[1])
        if rounds <= 0:
            color_print("yellow", "Number of rounds must be a positive integer.")
            return
    except ValueError:
        color_print("yellow", "Invalid number of rounds. Please provide a valid integer.")
        return
    actor1_strat = sys.argv[2]
    actor2_strat = sys.argv[3]
    if actor1_strat not in available_strats or actor2_strat not in available_strats:
        color_print("yellow", "Invalid strategy. Available: \n- " + "\n- ".join(available_strats))
        return

    # play the game
    outcome = play_game(actor1_strat, actor2_strat, rounds)

    # print the output to the terminal
    color_print("magenta", "Prisoners' Dilemma")
    color_print("magenta", "────────────────────────")

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
    print()

    color_print("blue", "Victory strategy:")
    if outcome["actor1"] > outcome["actor2"]:
        victory_strat = actor1_strat
    elif outcome["actor1"] < outcome["actor2"]:
        victory_strat = actor2_strat
    else:
        victory_strat = "Tied"
    color_print("green", victory_strat)


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
