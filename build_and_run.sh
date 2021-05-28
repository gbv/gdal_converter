#!/bin/bash

sudo docker build --no-cache -t converter .
sudo docker run -d -p 5000:5000 --name converter converter
