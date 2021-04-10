#! /bin/bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


python3 -m pytest Service1 --cov=Service1 --cov-report=term-missing