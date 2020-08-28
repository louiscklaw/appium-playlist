#!/usr/bin/env bash

set -ex

reset

cd test_scripts
  yarn
  node helloworld.js

cd ..