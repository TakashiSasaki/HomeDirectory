#!/bin/bash
currentBranch=`git branch -a | awk '/\*.+/{print $2}'`
remotes=( `git branch -a | awk 'BEGIN{FS="/"} /.+\/.+\/.+/ {print $2}' | sort | uniq | awk '{printf $0}'` )
branches=`git branch -a | awk 'BEGIN {FS="/"} /.+\/.+\/.+/ {print $3}' | sort | uniq | awk '{printf "%s ",$1 }'`

echo host name = $HOSTNAME
echo currentBranch = ${currentBranch}
echo remotes = ${remotes[@]}
echo branches = ${branches[@]}
