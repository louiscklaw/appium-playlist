#!/usr/bin/env bash

set -ex

reset

cd test_scripts
  # yarn
  # node helloworld_hub.js

  yarn
  node helloworld.js

  pipenv sync
  pipenv run python3 ./test.py
cd ..