all: windows linux

windows:
	cat /mnt/c/Windows/System32/drivers/etc/hosts | ./hosts2sqlite3.py

linux:
	cat /etc/hosts | ./hosts2sqlite3.py

