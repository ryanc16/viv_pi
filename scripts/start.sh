#!/bin/bash
root=$(git rev-parse --show-toplevel)
cd $root

.venv/bin/python start.py