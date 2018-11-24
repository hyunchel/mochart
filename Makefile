.PHONY: clean test

auto-lint:
	yapf mochart tests -ri

lint:
	flake8 mochart tests

test: clean
	pytest
	python -m tests.docstrings

ci-test: clean
	pytest -m "not integration"
	python -m tests.docstrings

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test-release:
	rm -rf dist/
	python setup.py sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	rm -rf dist/

test-install:
	pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple mochart
