#!/bin/bash
root=$(git rev-parse --show-toplevel)
cd $root

echo "starting install"
echo "installing linux packages"
if [[ $(command -v apt) ]]; then
  xargs -ra packages.txt sudo apt install -y
elif [[ $(command -v yum) ]]; then
  #sudo yum install -y $(cat packages.txt)
  echo "** see instructions for installing linux packages"
elif [[ $(command -v pacman) ]]; then
  #sudo pacman -S - < packages.txt
  echo "** see instruction for installing linux packages"
else
  echo "** unsupported linux package manager"
  exit
fi

echo "checking python requirements"
if [[ ! $(command -v pipx) ]]; then
  echo "pipx not installed"
  python3 -m pip install --user pipx
  pipx --version
fi

if [[ ! $(command -v pyenv) ]]; then
  echo "pyenv is not installed"
  curl https://pyenv.run | bash &&
  echo "PATH=\$PATH:~/.pyenv/bin" >> ~/.bashrc &&
  source ~/.bashrc
  pyenv --version
fi

if [[ ! $(command -v pipenv) ]]; then
  echo "pipenv not installed"
  pipx install pipenv
  pipenv --version
fi

if [[ ! -d .venv/ ]]; then
  echo "create local venv"
  mkdir .venv
  touch .venv/.gitkeep
fi
echo "installing application dependencies"
pipenv install
echo "install complete"
