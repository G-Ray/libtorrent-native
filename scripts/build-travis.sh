#!/usr/bin/env bash

source ~/.nvm/nvm.sh

set -e -u

if [[ "$TRAVIS_OS_NAME" == "linux" ]]
then
    export CC=gcc-5
    export CXX=g++-5
fi

npm install
npm test
npm run prebuild

# node_modules/.bin/node-pre-gyp package
