.PHONY: clean test

auto-lint:
	yapf mochart tests -ri

lint:
	flake8 mochart tests

test: clean
	pytest
	python -m tests.docstrings

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
