#!/bin/sh

type n
if [ $? -eq 0 ]; then
  sudo n lts
  sudo npm install -g npm
  sudo npm update
  sudo n stable
  exit 0
fi

sudo apt-fast update
sudo apt-fast install npm
sudo npm install -g n
sudo n stable
sudo apt-fast remove npm node
sudo apt-get autoremove


