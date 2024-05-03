.phony: run test

test:
	@PYTHONPATH=$$(pwd) pytest tests

run:
	@python main.py
