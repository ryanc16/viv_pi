#!/bin/bash
pipenv run coverage run run_tests.py
## get result of last process
# echo "$?"
pipenv run coverage html