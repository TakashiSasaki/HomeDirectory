#!/bin/bash

function initialize (){
  currentBranch=`git branch -a | awk '/\*.+/{print $2}'`
  remotes=( `git branch -a |\
    awk 'BEGIN{FS="/"} /.+\/.+\/.+/ {print $2}' |\
    sort | uniq | awk '{printf $0}'` )
  branches=`git branch -a |\
    awk 'BEGIN {FS="/"} /.+\/.+\/.+/ {print $3}' |\
    sort | uniq | awk '{printf "%s ",$1 }'`
}

for i; do
  case $i in
    "-h"|"--help") 
      echo git-branch-hostname.sh renames the branch name to the hostname. ;
      echo usage: git-branch-hostname.sh \[-h\|--help] \[-t\|--test]
      exit 0;;
    "-t"|"--test")
      initialize
      if [ "$currentBranch" -e "$HOSTNAME" ]; then exit 0; else exit 1; fi
  esac
done

initialize
git branch -m $currentBranch $HOSTNAME


#echo host name = $HOSTNAME
#echo currentBranch = ${currentBranch}
#echo remotes = ${remotes[@]}
#echo branches = ${branches[@]}
