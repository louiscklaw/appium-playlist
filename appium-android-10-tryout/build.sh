#!/usr/bin/env bash
# build on mac for github

set -ex

echo "y" | $ANDROID_HOME/tools/bin/sdkmanager --install 'system-images;${{ matrix.ansdroid_api_ver }};google_apis;x86_64'

$ANDROID_HOME/tools/bin/sdkmanager --list
$ANDROID_HOME/tools/bin/avdmanager list
