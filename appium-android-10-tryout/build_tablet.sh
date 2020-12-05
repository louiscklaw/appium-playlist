#!/usr/bin/env bash

set -ex

ACTIVE_ANDROID_NAME=tablet_a
ACTIVE_ADB_ANDROID='adb -s emulator-5562'

# adb -s emulator-5562 emu kill

echo "create a tablet device start"

echo "no" | $ANDROID_HOME/tools/bin/avdmanager create avd --device "Nexus 10" -n $ACTIVE_ANDROID_NAME -k 'system-images;android-30;google_apis;x86_64' --force --sdcard 512M

# nohup $ANDROID_HOME/emulator/emulator -avd $ACTIVE_ANDROID_NAME -no-snapshot > /dev/null 2>&1 &
nohup $ANDROID_HOME/emulator/emulator -avd $ACTIVE_ANDROID_NAME -no-snapshot &

$ANDROID_HOME/platform-tools/$ACTIVE_ADB_ANDROID wait-for-device shell 'while [[ -z $(getprop sys.boot_completed | tr -d '\r') ]]; do sleep 1; done; input keyevent 82'
echo "create a tablet device end"

echo $ANDROID_HOME/emulator/emulator -list-avds


while [ "$($ACTIVE_ADB_ANDROID shell getprop sys.boot_completed | tr -d '\r')" != "1" ]; do
  echo "Still waiting for boot.."
  sleep 1
done

echo 'boot tablet done'

exit 0
