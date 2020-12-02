#!/usr/bin/env bash

set -ex

# yarn add global appium
# yarn add global appium-doctor

node ./index.js

# pipenv sync

adb shell content insert --uri content://settings/system --bind name:s:show_touches --bind value:i:1


pipenv run python3 ./main.py
