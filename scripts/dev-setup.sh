#!/bin/bash
root=$(git rev-parse --show-toplevel)
cd $root

echo "checking development requirements"
pipx --version
if [[ $? != 0 ]]; then
  echo "pipx not installed"
  python3 -m pip install --user pipx
fi
pipenv --version
if [[ $? != 0 ]]; then
  echo "pipenv not installed"
  pipx install pipenv
fi
pyenv --version
if [[ $? != 0 ]]; then
  echo "pyenv is not installed"
  curl https://pyenv.run | bash &&
  echo "PATH=\$PATH:~/.pyenv/bin" >> ~/.bashrc &&
  exec $SHELL
fi