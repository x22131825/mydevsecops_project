#!/usr/bin/env bash


sudo apt update
sudo apt install ruby-full
sudo apt install wget

wget https://aws-codedeploy-eu-west-1.s3.eu-west-1.amazonaws.com/latest/install

chmod +x ./install
sudo ./install auto > /tmp/logfile
sudo service codedeploy-agent status
sudo service codedeploy-agent status

sudo apt install -y python3-pip
sudo apt install -y nginx
sudo apt install -y virtualenv

