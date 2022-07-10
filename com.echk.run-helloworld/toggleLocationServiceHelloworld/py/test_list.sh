#!/usr/bin/env bash

#set -ex

for ((i = 0 ; i < 99 ; i++)); do
  echo $i
  pipenv run pytest -s
done

