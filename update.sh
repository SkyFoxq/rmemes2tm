#!/bin/bash
HOME=/root
LOGNAME=root
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/root
cd "$(dirname "$0")"
source ./venv/bin/activate
rm memes.json
scrapy crawl rmemes -o memes.json

