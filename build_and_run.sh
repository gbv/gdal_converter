#!/bin/bash

sudo docker stop converter
sudo docker container rm converter
sudo docker build --no-cache -t converter .
sudo docker run -d -p 5000:5000 --name converter converter
sudo docker network connect easydb_default converter
