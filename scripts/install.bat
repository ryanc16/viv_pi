echo off
echo "configuring for windows"
if not exist .venv\ (
  echo "create local venv"
  mkdir .venv
  type NUL > .venv\.gitkeep
)
echo "activating and installing requirements"
pipenv install