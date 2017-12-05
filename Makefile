all: windows linux

windows:
	cat hosts.windows | ./hosts2sqlite3.py

linux:
	cat /etc/hosts | ./hosts2sqlite3.py

