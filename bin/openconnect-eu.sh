#!/bin/sh
PATH=$HOME/bin:$PATH
cat ~/.openconnect.enc | openssl-rsautl-decrypt.sh | sudo openconnect -u sasaki.takashi.mg --passwd-on-stdin vpn1.ehime-u.ac.jp --background

sleep 3

sudo ip route del default dev tun0 scope link
#ip route del 133.71.254.4/32 dev eth0
sudo ip route add 133.71.3.0/24 dev tun0 scope link
sudo ip route add 133.71.0.0/16 dev tun0 scope link
route -n


