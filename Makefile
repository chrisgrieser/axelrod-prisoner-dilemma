.PHONY: setup docs run run_all
#───────────────────────────────────────────────────────────────────────────────

run_all: # basic testrun
	export IS_MAKE=1 && \
	source ./.venv/bin/activate && \
	python3 ./prisoner_dilemma_main.py "tit_for_tat" "unforgiving"

run: # basic testrun
	export IS_MAKE=1 && \
	source ./.venv/bin/activate && \
	python3 ./prisoner_dilemma_main.py --all

setup: # set up virtual environment and install dependencies
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate && \
	pip3 install -r requirements.txt

docs: # browse docs
	source ./.venv/bin/activate && \
	pdoc ./src/*.py

