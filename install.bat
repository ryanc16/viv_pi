echo off
echo "configuring for windows"
if not exist .venv\pyvenv.cfg (
  echo "building venv"
  python -m venv .venv
)
echo "activating and installing requirements"
.venv\Scripts\activate.bat && pipenv install