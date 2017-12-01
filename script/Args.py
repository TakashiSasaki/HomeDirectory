#!/usr/bin/python3
import sys,re,copy,json

args = {}
orphanedKeys = []
orphanedValues = []

def setTemplate(template):
  args = copy.deepcopy(template)


def readArgs(argv=None):
  if argv is None: 
    argv = sys.argv
  
  i=1
  while i < len(argv):
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
  allStdin = sys.stdin.read()
  template = json.loads(allStdin)
  setTemplate(template)
  readArgs()
  print("template = %s" % template)
  print("orphanedKeys = %s" % orphanedKeys) 
  print("orphanedValues = %s" % orphanedValues)

