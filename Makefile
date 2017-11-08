all: windows linux

windows:
	./cat-windows-hosts | ./hosts2sqlite3

linux:
	./cat-linux-hosts | ./hosts2sqlite3

