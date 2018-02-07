#!/bin/sh
PATH=$HOME/bin:$PATH

while true; do

	sleep 60
	sudo ip route del default dev tun0 scope link
	#ip route del 133.71.254.4/32 dev eth0
	sudo ip route add 133.71.3.0/24 dev tun0 scope link
	sudo ip route add 133.71.0.0/16 dev tun0 scope link
	route -n

done
