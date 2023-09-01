.PHONY: setup docs test
#───────────────────────────────────────────────────────────────────────────────

setup: # set up virtual environment and install dependencies
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate && \
	pip3 install -r requirements.txt

docs: # browse docs
	source ./.venv/bin/activate && \
	pdoc ./src/*.py

