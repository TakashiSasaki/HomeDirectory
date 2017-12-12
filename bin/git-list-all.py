#!/usr/bin/python3 
import git,sys,os,copy,argparse,json


def doTree(tree, leadingPath):
  thisPath = copy.deepcopy(leadingPath)
  thisPath.append(tree.name)
  yield {"type": tree.type, "path": thisPath}

  for o in tree:
    if isinstance(o, git.objects.submodule.base.Submodule):
      yield doSubmodule(o, thisPath)
    if isinstance(o, git.objects.tree.Tree):
      doTree(o, thisPath)
    if isinstance(o, git.objects.tree.Blob):
      yield doBlob(o, thisPath)

  for o in tree.trees:
    if isinstance(o, git.objects.submodule.base.Submodule):
      yield doSubmodule(o, thisPath)
    if o is not tree and isinstance(o, git.objects.tree.Tree):
      doTree(o, thisPath)
    if isinstance(o, git.objects.blob.Blob):
      yield doBlob(o, thisPath)

def doSubmodule(submodule, leadingPath):
  thisPath = copy.deepcopy(leadingPath)
  try: 
    thisPath.append(submodule.name)
    return {"type": submodule.type, "path": thisPath}
  except Exception as e:
    return {"type": submodule.type, "path": thisPath} 

def doBlob(blob, leadingPath):
  thisPath = copy.deepcopy(leadingPath)
  thisPath.append(blob.name)
  return {"type": blob.type, "path": thisPath}

def doCommit(commit):
  generator = doTree(commit.tree, [])
  generator
  for x in generator:
    x["commit"] = commit.hexsha
    print("\x1e"+json.dumps(x)+"\x0a")

argumentParser = argparse.ArgumentParser(allow_abbrev=True)
argumentParser.add_argument("gitDirectory", default=".")
argumentParser.add_argument("--interactive", 
  action="store_true", default=False, help="enter interactive mode") 
argument = argumentParser.parse_args()


repo = git.Repo(argument.gitDirectory)
for ref in repo.refs:
  doCommit(ref.commit)
  for parent in ref.commit.parents:
    doCommit(parent)

import code
if argument.interactive:
  code.interact(local=locals())

