#!/usr/bin/env bash

set -ex

docker compose kill
docker compose down

docker compose rm -s -f -v
