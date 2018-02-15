#!/bin/sh
type apt-fast
if [ $? -gt 0 ]; then
  sudo apt install apt-fast -y
fi

if [ -e /etc/debian_version ]; then
  sudo apt-fast update
  sudo apt-fast upgrade -y

  type sqlite; if [ $? -gt 0 ]; then sudo apt-fast install sqlite -y; fi
  type sqlite3; if [ $? -gt 0 ]; then sudo apt-fast install sqlite3 -y; fi
fi

type python3
if [ $? -eq 0 ]; then
  python3 -c "import git"
  if [ $? -gt 0 ]; then
    sudo apt-fast install python3-git -y
  fi
  python3 -c "import apt_pkg"
  if [ $? -gt 0 ]; then
    sudo apt-fast install python3-apt python3-apt-dbg -y
  fi
fi


