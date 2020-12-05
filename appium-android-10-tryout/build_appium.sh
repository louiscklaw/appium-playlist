#!/usr/bin/env bash

set -ex

npm install appium

./node_modules/.bin/appium \
  --log-timestamp \
  --log-no-colors \
  --allow-insecure chromedriver_autodownload > appium.log &
