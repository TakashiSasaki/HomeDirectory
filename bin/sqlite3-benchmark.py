#!/usr/bin/python3 -i
import tempfile,os,sqlite3,random,time

def insert(nRows):
  startTime = time.time()
  random.seed()
  tempPath = tempfile.mkstemp()[1]
  connection = sqlite3.connect(tempPath);
  cursor = connection.execute("CREATE TABLE test (n REAL)")
  for x in range(nRows):
    cursor.execute("INSERT INTO test (n) VALUES (?)", [random.random()])
  connection.commit()
  cursor = connection.execute("SELECT rowid,* FROM test")
  rows = cursor.fetchall()
  print("inserted and fetched %s rows in %ss" % (len(rows), time.time()-startTime))
  os.unlink(tempPath)

insert(100)
insert(1000)
insert(10000)

