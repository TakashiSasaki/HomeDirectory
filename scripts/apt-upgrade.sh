#!/bin/sh
if [ -e /etc/debian_version ]; then
  sudo apt update
  sudo apt upgrade -y

  type sqlite; if [ $? -gt 0 ]; then sudo apt install sqlite; fi
  type sqlite3; if [ $? -gt 0 ]; then sudo apt install; fi
fi

type python3
if [ $? -eq 0 ]; then
  python3 -c "import git"
  if [ $? -gt 0 ]; then
    sudo apt install python3-git -y
  fi
  python3 -c "apt_pkg"
  if [ $? -gt 0 ]; then
    sudo apt install python3-apt python3-apt-dbg -y
  fi
fi

