#!/usr/bin/env bash

set -ex

docker-compose pull

docker-compose build

docker-compose up
