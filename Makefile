.PHONY: init docs run run_all help
#───────────────────────────────────────────────────────────────────────────────

run: # "tit_for_tat" vs "unforgiving"
	source ./.venv/bin/activate && \
	python3 prisoner_dilemma/main.py "tit_for_tat" "unforgiving"

run_all: # run battle royal
	source ./.venv/bin/activate && \
	python3 prisoner_dilemma/main.py --all

help:
	source ./.venv/bin/activate && \
	python3 prisoner_dilemma/main.py --help

init: # set up venv & install deps
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate && \
	pip3 install -r requirements.txt

docs: # generate pdoc
	source ./.venv/bin/activate && \
	pdoc ./*.py

