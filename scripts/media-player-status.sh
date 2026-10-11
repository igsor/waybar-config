#!/usr/bin/env bash

INTERVAL="1s"

while :; do

    STATUS=$(mpc status "%state%")

    if [ "$STATUS" == "playing" ]; then
        echo "󰝚"
    elif [ "$STATUS" == "paused" ]; then
        echo "󰝛"
    elif [ "$STATUS" == "stopped" ]; then
        echo "󰝛"
    else
        echo "󰝛"
    fi

    sleep $INTERVAL

done
