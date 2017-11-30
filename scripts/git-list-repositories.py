#!/usr/bin/python3
import git,sys,os

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


