#!/bin/sh
if [ $1 -e "-h" ]; then
  echo "encrypt stdin by id_rsa."
  exit 0
fi
openssl rsautl -encrypt -inkey $HOME/.ssh/id_rsa
