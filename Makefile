.PHONY: setup docs test
#───────────────────────────────────────────────────────────────────────────────

test: # simple test run
	python3 prisoners-dilemma.py 5 "unforgiving" "always_defect"

setup: # set up virtual environment and install dependencies
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip3 install -r requirements.txt

docs: # generate documentation
	rm -rf ./docs ; \
	pdoc *.py --output-directory=./docs && \
	open ./docs/index.html

