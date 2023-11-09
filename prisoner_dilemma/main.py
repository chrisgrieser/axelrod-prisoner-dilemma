"""Simple simulation of the prisoner's dilemma experiment.

Inspired by Axelrod's "Evolution of Cooperation" (1984).
Prior software: https://github.com/Axelrod-Python/Axelrod
"""

from __future__ import annotations

from sys import argv

import pandas as pd
import strategies
from parameters import punishment_years as punishment
from parameters import rounds_to_play as rounds
from preview import preview_html

# ──────────────────────────────────────────────────────────────────────────────


def shell_help() -> None:
    """Print help message."""
    print("Usage: ")
    print(main.__doc__)
    print("Available Strategies: ")
    print(strategies.describe_all_strategies())


def winner_of_outcome(outcome_years: dict[str, int]) -> str:
    """Return the winner of the outcome."""
    strats = list(outcome_years.keys())
    if outcome_years[strats[0]] < outcome_years[strats[1]]:
        return strats[0]
    if outcome_years[strats[0]] > outcome_years[strats[1]]:
        return strats[1]
    return "Tied"


def play_game(strats: tuple[str, str]) -> dict[str, int]:
    """Play prisoners' dilemma and return the accumulated outcome for all rounds.

    Args:
        strats: Tuple of two strategies, the position is implicitly the id of the actor.

    Returns:
        dict of strategies and their accumulated years

    [Outcomes are based on the archetypical prisoner's
    dilemma.](https://www.wikiwand.com/en/Prisoner's_dilemma#Strategy_for_the_prisoner's_dilemma)
    """
    total_years = [0, 0]
    run_history: list[tuple[str, str]] = []

    for _ in range(rounds):
        actions = (
            strategies.strategy_funcs[strats[0]](0, run_history),
            strategies.strategy_funcs[strats[1]](1, run_history),
        )
        if actions[0] == "cooperate" and actions[1] == "cooperate":
            total_years[0] += punishment["both_cooperate"]
            total_years[1] += punishment["both_cooperate"]
        elif actions[0] == "defect" and actions[1] == "defect":
            total_years[0] += punishment["both_defect"]
            total_years[1] += punishment["both_defect"]
        elif actions[0] == "cooperate" and actions[1] == "defect":
            total_years[0] += punishment["loose"]
            total_years[1] += punishment["win"]
        elif actions[0] == "defect" and actions[1] == "cooperate":
            total_years[0] += punishment["win"]
            total_years[1] += punishment["loose"]
        run_history.append(actions)

    # transform simple array into dict
    outcome_years = {
        strats[0]: total_years[0],
        strats[1]: total_years[1],
    }
    return outcome_years


def battle_royale() -> None:
    """Play the battle royale, i.e., every strategy against every other strategy.

    Creates html file, containing a matrix of strategies vs strategies, and the
    accumulated punishment over rounds.
    """
    overall_matrix: list[list[str]] = []
    total_punishment: dict[str, int] = {}

    for strategy in strategies.list_all:
        total_punishment[strategy] = 0

    for strategy_row in strategies.list_all:
        overall_matrix.append([])
        row_num = len(overall_matrix)
        cur_row_matrix = overall_matrix[-1]

        for strategy_col in strategies.list_all:
            # prevent duplicate fights and fights of the strategy against itself
            col_num = len(cur_row_matrix) + 1
            if col_num >= row_num:
                cur_row_matrix.append("")
                continue

            outcome_years = play_game((strategy_row, strategy_col))

            # update matrix
            winner_strat = winner_of_outcome(outcome_years)
            cur_row_matrix.append(winner_strat)

            # update total punishment count
            total_punishment[strategy_row] += outcome_years[strategy_row]
            total_punishment[strategy_col] += outcome_years[strategy_col]

    header = list(strategies.list_all)
    matrix_frame = pd.DataFrame(
        overall_matrix,
        columns=header,
        index=header,
    )
    punishment_frame = pd.DataFrame(
        list(total_punishment.items()),
        columns=["Strategy", "Punishment"],
        index=None,
    )

    total_rounds = rounds * (len(strategies.list_all) - 1)
    html: str = (
        "<h3>Prisoner's Dilemma Strategies</h3>"
        "<i>Battle Royale: every strategy against every other strategy "
        f" ({rounds} rounds)</i>.<br><br>"
        + strategies.describe_all_strategies().replace("\n", "<br>")
        + "<br>"
        + matrix_frame.to_html()
        + "<br>"
        f"<h4>Accumulated Punishment over {total_rounds} rounds</h4>"
        + punishment_frame.to_html()
        + "<br>"
    )

    preview_html(html)


def one_game_output(strats_used: tuple[str, str]) -> None:
    """Play the regular game, i.e., one strategy against another strategy.

    Outputs the outcome of the game to the terminal.
    """
    outcome_years = play_game(strats_used)
    victory_strat = winner_of_outcome(outcome_years)

    # print the output to the terminal
    print("PRISONERS' DILEMMA")
    print("────────────────────────")

    print("STRATEGIES:")
    print("Actor 1:", strats_used[0])
    print("Actor 2:", strats_used[1])
    print()

    print("ROUNDS:")
    print(rounds)
    print()

    print("OUTCOME:")
    print(f"Actor 1: {outcome_years[strats_used[0]]} years")
    print(f"Actor 2: {outcome_years[strats_used[1]]} years")
    print()

    print("VICTORY STRATEGY:")
    print(victory_strat)


def main() -> None:
    """Play the prisoner's dilemma.

    ```bash
    # Main Usage (Output to terminal):
    python3 prisoner_dilemma/main.py "actor_1_strategy" "actor_2_strategy"

    # Battle Royale — every strategy against every strategy (Output to html):
    python3 prisoner_dilemma/main.py --all

    # Help
    python3 prisoner_dilemma/main.py --help
    ```
    """
    # --help
    no_parameter = len(argv) == 1
    if no_parameter or argv[1] == "--help" or argv[1] == "-h":
        shell_help()
        return

    # --all: BATTLE ROYALE
    if argv[1] == "--all":
        battle_royale()
        return

    # PLAY A REGULAR GAME
    # read & validate input
    parameters_needed = 2
    if len(argv) < parameters_needed + 1:  # +1, as argv[0] is script name
        print("Expected parameters: <actor1_strategy> <actor2_strategy>")
        return

    strats_used = (argv[1], argv[2])
    for strategy in strats_used:
        if strategy not in strategies.list_all:
            msg = f"Strategy '{strategy}' is invalid. Available strategies are:"
            msg += "\n- " + "\n- ".join(strategies.list_all)
            print(msg)
            return
    if argv[1] == argv[2]:
        print("Actor 1 and Actor 2 cannot be the same.")
        return

    one_game_output(strats_used)


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
