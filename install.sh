#!/bin/bash

echo "OS: $OSTYPE"
if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" && "$OSTYPE" != "cygwin" ]]; then
# some version of linux
  echo "configuring for linux"
  if [[ ! -f .venv/pyvenv.cfg ]]; then
    echo "building venv"
    python3 -m venv .venv
  fi
  echo "installing linux dependencies"
  xargs sudo apt-get install -y < packages.txt
  echo "activating and installing requirements"
  source .venv/bin/activate && python -m pip install pipenv && pipenv install
else
# assume its windows
  cmd "/C install.bat"
fi