#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install codedeploy-agent

sudo apt install -y python3-pip
sudo apt install -y nginx
sudo apt install -y virtualenv
sudo service codedeploy-agent start

sudo yum update codedeploy-agent
sudo service codedeploy-agent restart
