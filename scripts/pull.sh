#!/bin/bash
root=$(git rev-parse --show-toplevel)
cd $root

pi_user=$(cat ./keys/pi_user)
pi_ip=$(cat ./keys/pi_ip)
pi_dir="~/Projects/viv_pi"
scp -i ./keys/pi_rsa "$pi_user@$pi_ip:$pi_dir/$1" src/main/