#! /bin/bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


python3 -m pytest service1 --cov=service1 --cov-report=term-missing
python3 -m pytest service2 --cov=service2 --cov-report=term-missing
python3 -m pytest service3 --cov=service3 --cov-report=term-missing
python3 -m pytest service4 --cov=service4 --cov-report=term-missing