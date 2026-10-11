#!/usr/bin/env bash

zscroll \
    --length 20 \
    --delay 0.4 \
    --update-check true \
    --scroll-padding " | " \
    --eval-in-shell true \
    "mpc current -f '%title%' | sed -e 's/^$/<unknown>/'" 2>/dev/null

wait
