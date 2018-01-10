#!/bin/sh
PATH=$HOME/bin:$PATH

while true; do
	cat ~/.openconnect.enc | openssl-rsautl-decrypt.sh | sudo openconnect -u sasaki.takashi.mg --passwd-on-stdin vpn1.ehime-u.ac.jp

	sleep 20
	route -n
done
