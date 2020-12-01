#!/usr/bin/env bash

set -ex

sudo mkdir -p /usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver
sudo chmod 777 /usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver

appium --allow-insecure chromedriver_autodownload