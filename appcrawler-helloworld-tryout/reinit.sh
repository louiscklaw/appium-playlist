#!/usr/bin/env bash

set -ex

pipenv --rm |true
pipenv sync
