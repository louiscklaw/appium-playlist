#!/usr/bin/env bash

set -ex

pipenv sync

pipenv run python3 ./appium-helloworld.py
