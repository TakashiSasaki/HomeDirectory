#!/bin/sh
locate -r "\\.git$" | sed -e "s/\\.git$//g" | while read line; do
  if [ -d "$line"/.git ]; then
    echo $line
  fi
done



