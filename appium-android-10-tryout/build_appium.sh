#!/usr/bin/env bash

set -ex

npm install appium@1.15.0

./node_modules/.bin/appium --log-timestamp --log-no-colors --allow-insecure chromedriver_autodownload > appium.log &
