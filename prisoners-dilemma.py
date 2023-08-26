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


def strategy_is_valid(strategy: str) -> bool:
    """Check whether the given strategy is available."""
    return strategy_to_action(0, strategy, []) != ""


def strategy_to_action(
    actor_self_id: int, strategy: str, previous_runs: list[tuple[str, str]],
) -> str:
    """Given the actors idendity, their strategy, and the previous rounds.

    If an invalid strategy is provided, returns empty string.
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


def play_game(strats: tuple[str, str], rounds: int) -> list[int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds.

    Outcomes are based on the archetypical prisoner's dilemma:
    https://www.wikiwand.com/en/Prisoner's_dilemma#Strategy_for_the_prisoner's_dilemma
    """
    years_in_prison = [0, 0]  # accumulate outcomes
    run_history = []  # keep track of previous rounds, i.e. a memory for the actors

    for _ in range(rounds):
        actions = (
            strategy_to_action(0, strats[0], run_history),
            strategy_to_action(1, strats[1], run_history),
        )
        if actions[0] == "cooperate" and actions[1] == "cooperate":
            years_in_prison[0] += 1
            years_in_prison[1] += 1
        elif actions[0] == "defect" and actions[1] == "defect":
            years_in_prison[0] += 2
            years_in_prison[1] += 2
        elif actions[0] == "cooperate" and actions[1] == "defect":
            years_in_prison[0] += 3
            years_in_prison[1] += 0
        elif actions[0] == "defect" and actions[1] == "cooperate":
            years_in_prison[0] += 0
            years_in_prison[1] += 3
        run_history.append(actions)

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
            color_print("yellow", "Number of rounds must be a positive number.")
            return
    except ValueError:
        color_print("yellow", "Number of rounds must be a number.")
        return
    strats_used = (sys.argv[2], sys.argv[3])
    if not strategy_is_valid(strats_used[0]) or not strategy_is_valid(strats_used[1]):
        color_print("yellow", "Invalid strategy.")
        return

    # play the game
    outcome_years = play_game(strats_used, rounds)

    # print the output to the terminal
    color_print("magenta", "Prisoners' Dilemma")
    color_print("magenta", "────────────────────────")

    color_print("blue", "Strategies:")
    print("Actor 1:", strats_used[0])
    print("Actor 2:", strats_used[1])
    print()

    color_print("blue", "Rounds:")
    print(rounds)
    print()

    color_print("blue", "Outcome:")
    print(f"Actor 1: {outcome_years[0]} years")
    print(f"Actor 2: {outcome_years[1]} years")
    print()

    color_print("blue", "Winner:")
    if outcome_years[0] > outcome_years[1]:
        victory_strat = strats_used[0]
    elif outcome_years[0] < outcome_years[1]:
        victory_strat = strats_used[1]
    else:
        victory_strat = "Tied"
    color_print("green", victory_strat)


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
