# Axelrod Prisoner's Dilemma
Simple Recreation of the prisoner's dilemma model from Axelrod's "Evolution of Cooperation".

Usage via command line:

```bash
# install dependencies
make setup
```

```bash
# activate virtual environment
source ./.venv/bin/activate

# show API docs
make docs

# Main Usage (Output to terminal):
./src/prisoner_dilemma_main.py "actor1_strategy" "actor2_strategy"

# Battle Royale — every strategy against every strategy (Output to html):
./src/prisoner_dilemma_main.py --all

# Help
./src/prisoner_dilemma_main.py --help
```

## Output
for `--all` (Battle Royal):

<img width="1178" alt="Pasted image 2023-08-28 at 18 26 01@2x" src="https://github.com/chrisgrieser/axelrod-prisoner-dilemma/assets/73286100/a5232774-5272-48f2-9153-2bf91e4f7ddb">
