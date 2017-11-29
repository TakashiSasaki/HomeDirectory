#!/bin/sh
locate -r "\\.git$" | sed -e "s/\\.git$//g"

