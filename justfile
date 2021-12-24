#!/usr/bin/env just --justfile

# install development dependencies
install-dev-deps:
  #!/usr/bin/env bash
  set -euxo pipefail
  python -m pip install --upgrade pip
  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
  if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

docs-serve:
  mkdocs serve

# MkDocs Publish
docs-publish:
  mkdocs gh-deploy --force

# Run all Lints
lint: codespell isort black flake8 mypy

codespell:
  codespell --skip="./.mypy_cache,./pytest_cache,.coverage,./htmlcov,./site,./.venv"

mypy:
  mypy

isort:
  isort .

black:
  black .

flake8:
  #!/usr/bin/env bash
  set -euxo pipefail
  # stop the build if there are Python syntax errors or undefined names
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
  # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
  flake8 . --count --statistics

test-with-cov:
  pytest --cov --doctest-modules --cov-report html

test:
  pytest --doctest-modules

check: lint test

push: check
  #!/usr/bin/env bash
  set -euxo pipefail
  ! git branch | grep '* main'
  git push origin

pr TITLE='' BODY='' PROJECT='Algorithms':
  gh pr create --base main --assignee @me --title "{{ TITLE }}" --body "{{ BODY }}" --project "{{ PROJECT }}" --web

# clean up feature branch BRANCH
done BRANCH=`git rev-parse --abbrev-ref HEAD`:
  #!/usr/bin/env bash
  set -euxo pipefail
  git checkout main
  git diff --no-ext-diff --quiet --exit-code
  git pull --rebase github main
  git diff --no-ext-diff --quiet --exit-code {{BRANCH}}
  git branch -D {{BRANCH}}

# A polyglot recipe
polyglot:
  #!/usr/bin/env python3 -v
  import sys, platform, time
  print(sys.version,  platform.version())
  print('Hello from python!')
  time.sleep(5)
