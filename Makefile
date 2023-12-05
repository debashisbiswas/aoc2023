.PHONY: test run shell

default: test

test:
	poetry run python -m unittest -v

run:
	poetry run python main.py

shell:
	poetry shell
