#!/usr/bin/env bash
set -x
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
rm -rf docs
mkdir -p ../docs
rm -rf wiki
git clone https://github.com/Netatalk/netatalk.wiki.git wiki

python3 convert.py

rm -rf wiki
