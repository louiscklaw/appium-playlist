#!/usr/bin/env bash

set -ex

echo 'testing python appium client'
pushd tests/python
  pipenv sync
  pipenv run python3 ./helloworld.py

popd

echo 'testing javascipt appium client'
pushd tests/javascript
  yarn
  node ./helloworld.js
popd
