.PHONY: clean test

lint:
	yapf mochart tests -ri

test: clean
	pytest
	python -m tests.docstrings

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
