#!/usr/bin/env bash

set -ex

trap 'catch' ERR EXIT KILL
catch() {
  echo 'exit script, shutdown docker...'
  scripts/down_docker.sh
}

scripts/down_docker.sh | true
scripts/start_docker.sh
sleep 90

test.sh
