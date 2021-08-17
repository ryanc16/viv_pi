pi_user=$(cat ./keys/pi_user)
pi_ip=$(cat ./keys/pi_ip)
pi_dir="~/Projects/viv_pi"
scp -i ./keys/pi_rsa -rp src/main/** "$pi_user@$pi_ip:$pi_dir/src/main/"
scp -i ./keys/pi_rsa start.py config.py "$pi_user@$pi_ip:$pi_dir/"