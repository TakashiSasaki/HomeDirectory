#!/bin/sh
PATH=$HOME/bin:$PATH
cat ~/.openconnect.enc | openssl-rsautl-decrypt.sh | sudo openconnect -u sasaki.takashi.mg --passwd-on-stdin vpn1.ehime-u.ac.jp 

