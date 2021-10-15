#!/bin/bash
root=$(git rev-parse --show-toplevel)
cd $root

echo "OS: $OSTYPE"
if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" && "$OSTYPE" != "cygwin" ]]; then
# some version of linux
  echo "configuring for linux"
  echo "installing linux dependencies"
  xargs sudo apt-get install -y < packages.txt
  if [[ ! -d .venv/ ]]; then
    echo "create local venv"
    mkdir .venv
    touch .venv/.gitkeep
  fi
  echo "activating and installing requirements"
  pipenv install
else
# assume its windows
  cmd "/C install.bat"
fi