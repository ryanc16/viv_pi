#!/bin/bash
root=$(git rev-parse --show-toplevel)
cd $root

pipenv run coverage run run_tests.py
## get result of last process
# echo "$?"
pipenv run coverage html