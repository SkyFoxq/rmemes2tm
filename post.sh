#!/bin/bash
cd "$(dirname "$0")"
source ./venv/bin/activate
python3 post_in_tm.py $1

