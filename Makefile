.PHONY: setup, docs
#───────────────────────────────────────────────────────────────────────────────

setup:
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip3 install -r requirements.txt

docs:
	pdoc *.py --output-directory=./docs

