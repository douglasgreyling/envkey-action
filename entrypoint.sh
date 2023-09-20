#!/usr/bin/env bash
set -e

echo 'running envkey-load.py'
python3 /envkey-load.py

echo 'loading secrets.sh'
bash /tmp/secrets.sh

echo 'loading masks.sh'
bash /tmp/masks.sh

rm -f /tmp/secrets.sh
rm -f /tmp/masks.sh
