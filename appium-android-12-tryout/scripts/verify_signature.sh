#!/usr/bin/env bash

set -ex

# /usr/bin/java -Xmx1024M -Xss1m -jar /home/logic/Android/platform-tools/apksigner.jar verify --print-certs /home/logic/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v5.12.16.apk
/usr/bin/java \
  -jar /home/logic/Android/platform-tools/apksigner.jar verify \
  --print-certs /home/logic/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v5.12.16.apk
