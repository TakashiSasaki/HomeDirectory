#!/usr/bin/python3
import sys,re,sqlite3

def readHosts():
  pairs = []
  for x in sys.stdin:
    m = re.match("\s*([0-9.]+)\s*",x)
    if m is None: continue
    address = m.group(1)
    n = re.findall("[0-9a-zA-Z.-]+",x)
    for i in range(1,len(n)):
      pairs.append((address, n[i]))
  return pairs
#print(pairs)

connection = sqlite3.connect("hosts.sqlite3")

def createTable():
  try:
    cursor = connection.execute("SELECT * FROM hosts")
  except sqlite3.OperationalError as e:
    cursor = connection.execute("CREATE TABLE hosts (host, address, primary key(host, address))")
    cursor.close()

def insertHosts(hosts):
  cursor = connection.cursor()
  for host in hosts:
    try:
      cursor.execute("INSERT INTO hosts (host, address) VALUES (?,?)", host)
    except sqlite3.IntegrityError as e:
      sys.stderr.write("%s %s already exists.\n" % host)
  connection.commit()

if __name__ == "__main__":
  hosts = readHosts()
  print(hosts)
  createTable()
  insertHosts(hosts)

