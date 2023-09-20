#!/usr/bin/env bash
set -e

python3 /envkey-load.py

bash /tmp/secrets.sh

rm -f /tmp/secrets.sh
