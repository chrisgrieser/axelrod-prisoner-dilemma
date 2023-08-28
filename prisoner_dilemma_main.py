#!/usr/bin/env python3
"""Simple simulation of the prisoner's dilemma experiment.

Inspired by Axelrod's "Evolution of Cooperation" (1984).
Prior software: https://github.com/Axelrod-Python/Axelrod
"""

from __future__ import annotations

from sys import argv

import strategies

# ──────────────────────────────────────────────────────────────────────────────


def color_print(color: str, text: str) -> None:
    """Print colored text with ANSI escape codes for the terminal.

    if `--debug`, then print plain text
    """
    if argv[1] == "--debug":
        print(text)
        return

    colors = {
        "magenta": "\033[1;35m",  # ] -- FIX needed to fix confusing the indentationexpr
        "blue": "\033[1;34m",  # ]
        "green": "\033[1;32m",  # ]
        "yellow": "\033[1;33m",  # ]
        "red": "\033[1;31m",  # ]
        "reset": "\033[0m",  # ]
    }
    print(colors[color] + text + colors["reset"])


# ──────────────────────────────────────────────────────────────────────────────


def play_game(strats: tuple[str, str], rounds: int) -> list[int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds.

    Args:
        strats: Tuple of two strategies, the position is implicitly the id of the actor
        rounds: Number of rounds to play

    Returns:
        Accumulated outcome, i.e. the number of years in prison (higher = worse).

    [Outcomes are based on the archetypical prisoner's
     dilemma.](https://www.wikiwand.com/en/Prisoner's_dilemma#Strategy_for_the_prisoner's_dilemma)
    """
    years_in_prison = [0, 0]  # accumulate outcomes
    run_history: list[tuple[str, str]] = []  # keep track of previous rounds

    for _ in range(rounds):
        actions = (
            strategies.strategy_funcs[strats[0]](0, run_history),
            strategies.strategy_funcs[strats[1]](1, run_history),
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


def shell_help() -> None:
    """Print help message."""
    color_print("blue", "Usage: ")
    print("python3 prisoner_dilemma_main.py <rounds> <actor1_strategy> <actor2_strategy>")
    print()
    color_print("blue", "Available Strategies: ")
    print(strategies.describe_all_strategies())


def battle_royale() -> None:
    """Play the battle royale, i.e. every strategy against every other strategy."""
    color_print("blue", "Battle Royale: ")
    all_strats = strategies.list_all
    # TODO: implement


def regular_game(rounds: int, strats_used: tuple[str, str]) -> None:
    """Play the regular game, i.e. one strategy against another strategy.

    Outputs the outcome of the game to the terminal.
    """
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
    if outcome_years[0] < outcome_years[1]:
        victory_strat = strats_used[0]
    elif outcome_years[0] > outcome_years[1]:
        victory_strat = strats_used[1]
    else:
        victory_strat = "Tied"
    color_print("green", victory_strat)


def main() -> None:
    """Validate input, play the game, and print the output for the terminal.

    Main Usage:
    `python3 prisoner_dilemma_main.py <rounds> <actor1_strategy> <actor2_strategy>`

    Battle Royale (every strategy against every strategy):
    `python3 prisoner_dilemma_main.py --all`

    Help:
    `python3 prisoner_dilemma_main.py --help`
    """
    # --help
    if argv[1] == "--help" or argv[1] == "-h":
        shell_help()
        return

    # --all
    if argv[1] == "--all" or argv[1] == "-a":
        battle_royale()
        return

    if argv[1] == "--debug":
        regular_game(5, ("tit_for_tat", "alternate"))
        return

    # read & validate input
    parameters_needed = 3
    if len(argv) < parameters_needed + 1:  # +1, as argv[0] is script name
        color_print("yellow", "Expected parameters: <rounds> <actor1_strategy> <actor2_strategy>")
        return
    try:
        rounds = int(argv[1])
    except ValueError:
        rounds = 0

    if rounds <= 0:
        color_print("yellow", "Number of rounds must be a positive number.")
        return

    strats_used = (argv[2], argv[3])
    available_strats = strategies.strategy_funcs.keys()
    for strategy in strats_used:
        if strategy not in strategies.list_all:
            msg = f"Strategy '{strategy}' is invalid. Available strategies are:"
            msg += "\n- " + "\n- ".join(available_strats)
            color_print("yellow", msg)
            return

    # play a regular game
    regular_game(rounds, strats_used)


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
