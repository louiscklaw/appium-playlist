#!/usr/bin/env bash

set -ex

# yarn add global appium
# yarn add global appium-doctor

node ./index.js

pipenv sync
pipenv run python3 ./main.py
