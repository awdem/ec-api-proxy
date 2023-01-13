# EC API


## Install requirements

* Python 3.8
* Pipenv (`pip install Pipenv`)

## Installation

This section assumes a working python 3.8 environment with Pipenv installed.

* `cp ec_api/settings/local.py.example ec_api/settings/local.py`
* Install Python dependencies: `pipenv install --dev`
* Run the test suite: `pytest`
* Run lint checks: `pytest --flakes`
* Auto-format: `black .`

## Pre-commit

Using a pre-commit hook is suggested when working on this project to catch
code standard issues before committing them.

Install the hooks with:

`pre-commit install`


[![codecov](https://codecov.io/gh/DemocracyClub/ec-api-proxy/branch/hotfix/dependency-upgrades/graph/badge.svg?token=M9VDGSYISQ)](https://codecov.io/gh/DemocracyClub/ec-api-proxy)
