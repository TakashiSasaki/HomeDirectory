#!/usr/bin/python3
import sys,re,copy,json

args = {}
orphanedKeys = []
orphanedValues = []

def getArgs():
  global args
  return copy.deepcopy(args)

def getOrphanedKeys():
  global orphanedKeys
  return copy.deepcopy(orphanedKeys)

def getOrphanedValues():
  global orphanedValues
  return copy.deepcopy(orphanedValues)

def setTemplate(template):
  global args
  args = copy.deepcopy(template)

def readArgv(argv=None):
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
      if m1 in args:
        if args[m1] == True or args[m1] == False:
          args[m1] = True
          i += 1
          continue
        else:
          args[m1].append(argv[i+1])
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
  readArgv()
  print("args = %s" % getArgs())
  print("orphanedKeys = %s" % getOrphanedKeys()) 
  print("orphanedValues = %s" % getOrphanedValues())

