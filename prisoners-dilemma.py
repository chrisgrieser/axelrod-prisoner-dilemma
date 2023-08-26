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
    actor_self_id: int,
    strategy: str,
    previous_runs: list[tuple[str, str]],
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
    opponent_id = 1 if actor_self_id == 0 else 0
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
            last_self_action = previous_runs[-1][actor_self_id]
            action = "defect" if last_self_action == "cooperate" else "cooperate"
    elif strategy == "tit-for-tat":
        if is_first_run:
            action = "cooperate"
        else:
            last_opponent_action = previous_runs[-1][opponent_id]
            action = last_opponent_action

    return action


def play_game(actor1_strat: str, actor2_strat: str, rounds: int) -> list[int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds."""
    years_in_prison = [-1, 0, 0]  # first value dummy for one-based indexing
    run_history = []  # keep track of previous rounds, i.e. a memory for the actors

    for _ in range(rounds):
        actor1_action = strategy_to_action(1, actor1_strat, run_history)
        actor2_action = strategy_to_action(2, actor2_strat, run_history)
        # apply outcome rules for the prisoner's dilemma
        # DOCS https://www.wikiwand.com/en/Prisoner's_dilemma#Strategy_for_the_prisoner's_dilemma
        if actor1_action == "cooperate" and actor2_action == "cooperate":
            years_in_prison[1] += 1
            years_in_prison[2] += 1
        elif actor1_action == "defect" and actor2_action == "defect":
            years_in_prison[1] += 2
            years_in_prison[2] += 2
        elif actor1_action == "cooperate" and actor2_action == "defect":
            years_in_prison[1] += 3
            years_in_prison[2] += 0
        elif actor1_action == "defect" and actor2_action == "cooperate":
            years_in_prison[1] += 0
            years_in_prison[2] += 3
        run_history.append((actor1_action, actor2_action))

    return years_in_prison


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
    outcome_years = play_game(actor1_strat, actor2_strat, rounds)

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
    print(f"Actor 1: {outcome_years[1]} years")
    print(f"Actor 2: {outcome_years[2]} years")
    print()

    color_print("blue", "Victory strategy:")
    if outcome_years[1] > outcome_years[2]:
        victory_strat = actor1_strat
    elif outcome_years[1] < outcome_years[2]:
        victory_strat = actor2_strat
    else:
        victory_strat = "Tied"
    color_print("green", victory_strat)


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
