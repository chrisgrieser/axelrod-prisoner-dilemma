"""
Simple simulation of the prisoner's dilemma experiment by Axelrod 1984
"""

import sys

# ──────────────────────────────────────────────────────────────────────────────


def colored_print(color: str, text: str):
    colors = {
        "blue": "\033[1;34m",  # ] -- needed to fix confusing the indentationexpr
        "green": "\033[1;32m",  # ]
        "yellow": "\033[1;33m",  # ]
        "red": "\033[1;31m",  # ]
        "reset": "\033[0m",  # ]
    }
    print(colors[color] + text + colors["reset"])


def play_game(actor_1_strategy: str, actor_2_strategy: str, rounds: int):
    outcome = {"actor_1": 0, "actor_2": 0}
    for _ in range(rounds):
        if actor_1_strategy == "cooperate" and actor_2_strategy == "cooperate":
            outcome["actor_1"] += 1
            outcome["actor_2"] += 1
        elif actor_1_strategy == "defect" and actor_2_strategy == "defect":
            outcome["actor_1"] += 2
            outcome["actor_2"] += 2
        elif actor_1_strategy == "cooperate" and actor_2_strategy == "defect":
            outcome["actor_1"] += 3
            outcome["actor_2"] += 0
        elif actor_1_strategy == "defect" and actor_2_strategy == "cooperate":
            outcome["actor_1"] += 0
            outcome["actor_2"] += 3
    return outcome


def main():
    # config
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    # play the game
    actor_1_strategy = "defect"
    actor_2_strategy = "cooperate"
    outcome = play_game(actor_1_strategy, actor_2_strategy, rounds)

    # output
    colored_print("green", "Prisoners' Dilemma")
    colored_print("green", "──────────────────")

    colored_print("blue", "Strategies:")
    print("Actor 1:", actor_1_strategy)
    print("Actor 2:", actor_2_strategy)
    print()

    colored_print("blue", "Rounds:")
    print(rounds)
    print()

    colored_print("blue", "Outcome:")
    print(f"Actor 1: {outcome['actor_1']} years")
    print(f"Actor 2: {outcome['actor_2']} years")


# ──────────────────────────────────────────────────────────────────────────────

main()
