#!/usr/bin/env bash

set -ex

# troubleshoot, for app signing using java
export JAVA_TOOL_OPTIONS=""

appium server --allow-cors
