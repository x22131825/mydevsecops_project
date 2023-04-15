#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install django==2.1.15 -r /home/ubuntu/mydevsecproject/requirements.txt
