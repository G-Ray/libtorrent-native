#!/usr/bin/env bash
set -e

OPENSSL_VERSION="1.0.2k";
SHA256="6b3977c61f2aedf0f96367dcfb5c6e578cf37e7b8d913b4ecb6643c3cb88d8c0"

# check to see if openssl folder is empty
if [ ! -d "$HOME/openssl" ]; then
  wget "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz"
  # check SHA256
  echo "$SHA256  ./openssl-$OPENSSL_VERSION.tar.gz" | sha256sum -c
  tar xzvf "./openssl-$OPENSSL_VERSION.tar.gz" > /dev/null
  cd "./openssl-$OPENSSL_VERSION"
  ./config shared -fPIC --prefix="$HOME/openssl" --openssldir="$HOME/openssl"
  make && make install
else
  echo "Using cached openssl directory."
fi
