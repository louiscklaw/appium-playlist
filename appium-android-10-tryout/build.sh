#!/usr/bin/env bash
# build on mac for github

set -ex

ANDROID_NAMES=(\
  android_a \
  android_b \
  android_c \
  android_d \
  android_e \
  )
ADB_ANDROIDS=(\
  'adb -s emulator-5554' \
  'adb -s emulator-5556' \
  'adb -s emulator-5558' \
  'adb -s emulator-5560' \
  'adb -s emulator-5562' \
  )

echo "y" | $ANDROID_HOME/tools/bin/sdkmanager --install 'system-images;android-30;google_apis;x86_64'

$ANDROID_HOME/tools/bin/sdkmanager --list
$ANDROID_HOME/tools/bin/avdmanager list


for i in {0..3}
do
  echo ${ADB_ANDROIDS[$i]}
  echo ${ANDROID_NAMES[$i]}

  ACTIVE_ANDROID_NAME=${ANDROID_NAMES[$i]}
  ACTIVE_ADB_ANDROID=${ADB_ANDROIDS[$i]}

  echo "no" | $ANDROID_HOME/tools/bin/avdmanager create avd --device "pixel" -n $ACTIVE_ANDROID_NAME -k 'system-images;android-30;google_apis;x86_64' --force --sdcard 512M

  nohup $ANDROID_HOME/emulator/emulator -avd $ACTIVE_ANDROID_NAME -no-snapshot > /dev/null 2>&1 &

  $ANDROID_HOME/platform-tools/$ACTIVE_ADB_ANDROID wait-for-device shell 'while [[ -z $(getprop sys.boot_completed | tr -d '\r') ]]; do sleep 1; done; input keyevent 82'
done
