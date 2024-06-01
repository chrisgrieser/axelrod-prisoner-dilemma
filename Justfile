set quiet := true

run:
	source ./.venv/bin/activate && python3 -m prisoner_dilemma.main "tit_for_tat" "unforgiving"

run_battle_royale:
	source ./.venv/bin/activate && python3 -m prisoner_dilemma.main --all

help:
	source ./.venv/bin/activate && python3 -m prisoner_dilemma.main --help

init:
	[[ -d ./.venv ]] && rm -rf ./.venv
	python3 -m venv ./.venv
	source ./.venv/bin/activate && python3 -m pip install -r requirements.txt

docs:
	source ./.venv/bin/activate && pdoc ./*.py

