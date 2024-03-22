.PHONY: init docs run run_all help
#───────────────────────────────────────────────────────────────────────────────

# "tit_for_tat" vs "unforgiving"
run:
	source ./.venv/bin/activate && \
	python3 -m prisoner_dilemma.main "tit_for_tat" "unforgiving"

# run battle royal
run_all:
	source ./.venv/bin/activate && \
	python3 -m prisoner_dilemma.main --all

help:
	source ./.venv/bin/activate && \
	python3 -m prisoner_dilemma.main --help

# set up venv & install deps
init:
	[[ -d ./.venv ]] && rm -rf ./.venv ; \
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate && \
	python3 -m pip install -r requirements.txt

# generate pdoc
docs:
	source ./.venv/bin/activate && \
	pdoc ./*.py

