#!/usr/bin/env bash

set -ex

ACTIVE_ANDROID_NAME=${ANDROID_NAMES[4]}
ACTIVE_ADB_ANDROID=${ADB_ANDROIDS[4]}

echo "create a tablet device start"

echo "no" | $ANDROID_HOME/tools/bin/avdmanager create avd --device "Nexus 10" -n $ACTIVE_ANDROID_NAME -k 'system-images;android-30;google_apis;x86_64' --force --sdcard 512M
nohup $ANDROID_HOME/emulator/emulator -avd $ACTIVE_ANDROID_NAME -no-snapshot > /dev/null 2>&1 &
$ANDROID_HOME/platform-tools/$ACTIVE_ADB_ANDROID wait-for-device shell 'while [[ -z $(getprop sys.boot_completed | tr -d '\r') ]]; do sleep 1; done; input keyevent 82'
echo "create a tablet device end"

echo $ANDROID_HOME/emulator/emulator -list-avds
