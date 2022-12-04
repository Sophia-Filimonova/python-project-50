install:
	poetry install

lint:
	poetry run flake8 gendiff tests/

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff gendiff/scripts/ tests/ --cov-report xml 

selfcheck:
	poetry check

check: selfcheck lint test

gendiff:
	poetry run gendiff

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check gendiff build