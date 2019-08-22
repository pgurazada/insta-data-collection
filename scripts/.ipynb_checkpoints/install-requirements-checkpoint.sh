#! /bin/bash

# The following series of commands will be executed on a worker with 
# 0.6-1.5 GB RAM and OS Ubuntu 18.04 LTS

# This script should be run on the VM first before the data collection process

echo 'startup_message off' >> ~/.screenrc

sudo apt-get update && sudo apt-get -y upgrade

sudo apt-get install -y python3-pip

pip3 install instaloader tqdm

echo "Installed required packages"

mkdir data
mkdir data/raw
mkdir data/processed

# copy the list of instagram handles from the master machine. This should be placed in  the data/raw folder