#!/usr/bin/python3
import git,sys,os,argparse

parser = argparse.ArgumentParser(description="List git repositories.")
parser.add_argument("pathFile", nargs=1)
parser.add_argument("--stdin", action="store_true") 
namespace = parser.parse_args()
print(namespace)

for x in sys.stdin:
  repoPath = os.path.abspath(x.strip())
  try:
    repo = git.Repo(repoPath)
    print("  valid %s" % repoPath)
  except git.exc.InvalidGitRepositoryError as e:
    print("invalid %s" % repoPath)
  #try:
  #  head = repo.head
  #except ValueError as e:


