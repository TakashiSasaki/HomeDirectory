.PHONY: prepare

prepare:
	sudo apt-get update; sudo apt-get upgrade -y; sudo apt-get autoremove; \
		sudo n stable; sudo npm -g update; \
		git gc
