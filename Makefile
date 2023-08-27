.PHONY: setup docs test
#───────────────────────────────────────────────────────────────────────────────

test: # simple test run
	python3 prisoner-dilemma-main.py 5 "unforgiving" "always_defect"

setup: # set up virtual environment and install dependencies
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip3 install -r requirements.txt

docs: # browse docs
	pdoc *.py

