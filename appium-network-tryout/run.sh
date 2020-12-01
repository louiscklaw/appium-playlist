#!/usr/bin/env bash

set -ex

PROJ_HOME=$PWD/..

cd $PROJ_HOME/appium-android-10-tryout
  ./scripts/start_docker.sh
cd -

pipenv run python3 ./main.py
