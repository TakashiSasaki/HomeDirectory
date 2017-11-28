#!/bin/sh
if [ -e /etc/debian_version ]; then
  sudo apt update
  sudo apt upgrade -y

  type sqlite; if [ $? -gt 0 ]; then sudo apt install sqlite; fi
  type sqlite3; if [ $? -gt 0 ]; then sudo apt install; fi
fi

