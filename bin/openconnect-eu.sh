#!/bin/sh
cat ~/.openconnect.enc | ~/script/openssl-rsautl-decrypt.sh | sudo openconnect -u sasaki.takashi.mg --passwd-on-stdin vpn1.ehime-u.ac.jp 


