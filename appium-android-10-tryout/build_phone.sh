#!/usr/bin/env bash
# build on mac for github

set -ex

echo "y" | $ANDROID_HOME/tools/bin/sdkmanager --install 'system-images;android-30;google_apis;x86_64'

$ANDROID_HOME/tools/bin/sdkmanager --list
$ANDROID_HOME/tools/bin/avdmanager list

echo "no" | $ANDROID_HOME/tools/bin/avdmanager create avd --device "pixel" -n android_c -k 'system-images;android-30;google_apis;x86_64' --force --sdcard 512M

$ANDROID_HOME/emulator/emulator -avd android_c -no-snapshot &
# nohup $ANDROID_HOME/emulator/emulator -avd android_c -no-snapshot > /dev/null 2>&1 &

$ANDROID_HOME/platform-tools/adb -s emulator-5554 wait-for-device shell 'while [[ -z $(getprop sys.boot_completed | tr -d '\r') ]]; do sleep 5; done; input keyevent 82'


echo 'android phone start done'
exit 0
