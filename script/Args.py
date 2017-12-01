#!/usr/bin/python3

template = {}
orphanedKeys = []
orphanedValues = []

def setTemplate(template):
  template = template


def readArgs(argv=None):
  if argv is None: 
    import sys
    argv = sys.argv
  
  i=1
  while i < len(argv):
    import re
    m = re.match("^-(.+)$", argv[i])
    if m is None: 
      orphanedValues.append(argv[i])
      i += 1
      continue 
    else:
      m1 = m.group(1)
      if m1 in template:
        if template[m1] == True or template[m1] ==False:
          template[m1] = True
          i += 1
          continue
        else:
          template[m1].append(argv[i+1])
          i += 2
          continue
      else:
        orphanedKeys.append(m1) 
        i += 1
        continue
      

if __name__ == "__main__":
  import sys
  allStdin = sys.stdin.read()
  import json
  template = json.loads(allStdin)
  readArgs()
  print("template = %s" % template)
  print("orphanedKeys = %s" % orphanedKeys) 
  print("orphanedValues = %s" % orphanedValues)

