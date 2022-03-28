#!/usr/bin/env bash

set -ex

npm install appium

# install ffmpeg
brew install homebrew-ffmpeg/ffmpeg/ffmpeg

# opencv4nodejs cannot be found.
npm install -g opencv4nodejs

# mjpeg-consumer cannot be found.
npm install -g mjpeg-consumer

# set-simulator-location is not installed
brew install lyft/formulae/set-simulator-location


# idb and idb_companion are not installed
brew tap facebook/fb
brew install idb-companion
sudo pip3 install fb-idb

# ✖ applesimutils cannot be found
brew tap wix/brew
brew install applesimutils

# ✖ ios-deploy cannot be found
brew install ios-deploy


# ✖ bundletool.jar cannot be found


# ✖ gst-launch-1.0 and/or gst-inspect-1.0 cannot be found



npm install appium-doctor

./node_modules/.bin/appium-doctor

# ./node_modules/.bin/appium \
#   --log-timestamp \
#   --log-no-colors \
#   --allow-insecure chromedriver_autodownload > appium.log &
