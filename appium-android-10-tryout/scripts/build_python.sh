#!/usr/bin/envb bash

set -ex

python3 -V
python3 -m pip install pip --upgrade
python3 -m pip install pipenv
pipenv --version

cd github-android-emulator-tryout
  pipenv sync
cd -
