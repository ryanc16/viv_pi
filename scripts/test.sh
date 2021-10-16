#!/bin/bash
poetry run coverage run run_tests.py
## get result of last process
# echo "$?"
poetry run coverage html