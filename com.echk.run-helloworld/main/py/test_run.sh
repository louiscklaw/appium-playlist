#!/usr/bin/env bash

set -ex

for i in {1..10}
do
  pipenv run pytest -s
done