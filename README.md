# Axelrod Prisoner's Dilemma
Simple Recreation of the prisoner's dilemma model from Axelrod's "Evolution of
Cooperation."

Usage via command line:

```bash
# install dependencies
make init
```

```bash
# activate virtual environment
source ./.venv/bin/activate

# show API docs
make docs

# Main Usage (Output to terminal):
python3 prisoner_dilemma/main.py "actor1_strategy" "actor2_strategy"

# Battle Royale — every strategy against every strategy (Output to html):
python3 prisoner_dilemma/main.py --all

# Help
python3 prisoner_dilemma/main.py --help
```

## Output
for `--all` (Battle Royal):

<img width="1178" alt="Pasted image 2023-08-28 at 18 26 01@2x" src="https://github.com/chrisgrieser/axelrod-prisoner-dilemma/assets/73286100/a5232774-5272-48f2-9153-2bf91e4f7ddb">

## Recommended Citation

Please cite this software project as (APA):

```conf
Grieser, C. (2023). Simulation of Axelrod prisoner’s dilemma [Computer
software]. https://github.com/chrisgrieser/axelrod-prisoner-dilemma
```

For other citation styles, use the following metadata:
- [Citation File Format](./CITATION.cff)
- [BibTeX](./CITATION.bib)
