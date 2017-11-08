#!/usr/bin/python3
import sys,re,sqlite3

pairs = []
for x in sys.stdin:
  m = re.match("\s*([0-9.]+)\s*",x)
  if m is None: continue
  address = m.group(1)
  n = re.findall("[0-9a-zA-Z.-]+",x)
  for i in range(1,len(n)):
    pairs.append((address, n[i]))
#print(pairs)

connection = sqlite3.connect("hosts.sqlite3")
cursor = connection.cursor()
cursor.executemany("insert into hosts (host, address) values(?,?)", pairs)
connection.commit()

