#!/usr/bin/python3
import sys,re,os.path

def readHostsFile(file, hosts):
  tuples = []
  for x in file:
    m = re.match("^\s*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s+(\S+)\s*(\s*)$",x)
    if m is None: continue
    address = m.group(1)
    hostname = m.group(2)
    comment = m.group(3)
    tuples.append((address, hostname, comment))
    
  for address, hostname, comment in tuples:
    if address in hosts:
      if hostname in hosts[address]:
        hosts[address][hostname][comment] = None
      else:
        hosts[address][hostname] = {comment : None}
    else:
      hosts[address] = {hostname : {comment:None}}
  return hosts

if __name__ == "__main__":
  
  hosts = readHostsFile(sys.stdin, {})
  print(hosts)
  for address in hosts.keys():
    print(address)
    if os.path.exists(address):
      f = open(address, "r")
      hosts = readHostsFile(f, hosts)
      f.close()
    f = open(address, "w")
    for hostname in hosts[address].keys():
      for comment in hosts[address][hostname].keys():
        f.write(address + "\t" + hostname + "\t" + comment + "\n")
    f.close()

