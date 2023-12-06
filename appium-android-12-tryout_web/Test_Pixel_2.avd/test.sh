#!/usr/bin/env bash
# https://www.wrike.com/blog/how-to-create-an-android-emulator-terminal/

set -ex

export JAVA_TOOL_OPTIONS=""

# Step 7: Install the chosen image

# sdkmanager --list
yes | sdkmanager --install "system-images;android-30;google_apis_playstore;x86_64"
yes | sdkmanager --licenses

# # Step 8: Create the emulator

name=Test_Pixel_2_API_30
# echo no | avdmanager create avd --force --name $name --abi arm64-v8a --package 'system-images;android-30-ext5;google_apis_playstore;arm64-v8a'
echo no | avdmanager create avd --force -n $name -k "system-images;android-30;google_apis_playstore;x86_64"

cat ./config.ini > /home/logic/.android/avd/$name.ini

emulator -avd $name -no-snapshot -no-boot-anim -wipe-data
