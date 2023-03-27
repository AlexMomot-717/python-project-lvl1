install:
		poetry install

brain-games:
		poetry run brain-games

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-install-win:
		python -m pip install --user dist\hexlet_code-0.3.0-py3-none-any.whl

pre-commit:
		pre-commit run --all-files
