#!/usr/bin/env bash

set -ex

docker tag logickee/docker-android-x86-12.0 192.168.10.61:5500/docker-android-x86-12.0
docker push 192.168.10.61:5500/docker-android-x86-12.0