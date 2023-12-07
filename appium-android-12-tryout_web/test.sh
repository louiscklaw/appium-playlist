#!/usr/bin/env bash

set -ex

pipenv -v
python3 -V

trap 'catch' ERR EXIT KILL
catch() {
  echo 'exit script, shutdown docker...'
  scripts/down_docker.sh
}

scripts/down_docker.sh | true
scripts/start_docker.sh
sleep 90

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

sudo chown 1000:1000 -R video-nexus_12