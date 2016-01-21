#!/bin/sh

BASE_HOME=`pwd`
PORT=8100
LOCK_FILE="$BASE_HOME/log/webtail.lock"

start() {
    cd $BASE_HOME
    source env/bin/activate
    python webtail/webtail.py & >> log/webtail.log 2>&1;
    echo $! > $LOCK_FILE
}

start
