"""
Simple simulation of the prisoner's dilemma experiment by Axelrod 1984
"""

# ──────────────────────────────────────────────────────────────────────────────

config = {
    "rounds": 1,
}

game_history = []

# ──────────────────────────────────────────────────────────────────────────────


def play_game(actor_1_strategy: str, actor_2_strategy: str):
    outcome = {"actor_1": -1, "actor_2": -1}

    if actor_1_strategy == "cooperate" and actor_2_strategy == "cooperate":
        outcome["actor_1"] = 1
        outcome["actor_2"] = 1
    elif actor_1_strategy == "defect" and actor_2_strategy == "defect":
        outcome["actor_1"] = 2
        outcome["actor_2"] = 2
    elif actor_1_strategy == "cooperate" and actor_2_strategy == "defect":
        outcome["actor_1"] = 3
        outcome["actor_2"] = 0
    elif actor_1_strategy == "defect" and actor_2_strategy == "cooperate":
        outcome["actor_1"] = 0
        outcome["actor_2"] = 3

    return outcome


def main():
    print("Prisoners' Dilemma")
    print("──────────────────")

    actor_1_strategy = "defect"
    actor_2_strategy = "cooperate"
    print("Strategies")
    print("Actor 1:", actor_1_strategy)
    print("Actor 2:", actor_2_strategy)
    outcome = play_game(actor_1_strategy, actor_2_strategy)

    print()
    print("Outcome")
    print(f"Actor 1: {outcome['actor_1']} years")
    print(f"Actor 2: {outcome['actor_2']} years")


# ──────────────────────────────────────────────────────────────────────────────

main()
