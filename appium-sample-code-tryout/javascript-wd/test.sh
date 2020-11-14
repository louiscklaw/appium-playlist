#!/usr/bin/env bash

set -ex

export ANDROID_DEVICE_NAME=nexus_5_8.1
export ANDROID_PLATFORM_VERSION=8.1

# pushd test/basic
#   mocha android-basic-interactions.test.js
# popd

# mocha test/basic/helloworld.js
mocha --timeout 1500000 test/basic/android-basic-interactions.test.js