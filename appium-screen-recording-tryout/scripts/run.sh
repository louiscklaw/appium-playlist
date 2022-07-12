#!/usr/bin/env bash

set -ex

# yarn add global appium
# yarn add global appium-doctor

# node ./index.js

# pipenv run python3 ./main.py

mkdir -p /tmp/apk_pool

cp ./apk_pool/*.apk /tmp/apk_pool/

#pipenv run python3 ./test_ifconfig_me.py
pipenv run python3 ./test_curl.py
