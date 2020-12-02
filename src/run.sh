#!/bin/bash

# wait for wifi
i=0
while [ -z $(iwgetid -r) ]; do  # while SSID is null, do
    echo "No Wifi"
    i=$((i+1))
    sleep 1
    if [ $i -gt 100 ]
    then
      # timeout timeout after 100 seconds
      exit 0
    fi
done

if [ $(iwgetid -r) = "eduroam" ]
then
  # Run contact tracing script
  $HOME/PycharmProjects/TUcontact/venv/bin/python3 $HOME/PycharmProjects/TUcontact/src/main.py
fi
