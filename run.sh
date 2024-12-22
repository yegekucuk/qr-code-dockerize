#!/bin/bash

FILENAME=$1
DATA=$2
VERSION='latest'
echo "PARAMS: Filename $FILENAME, Data $DATA"

# Build the Docker image
docker build -t yegekucuk2/qr-dockerize:$VERSION .
echo "Successfully built image"

# Run the Docker container
docker rm -f qrcode && docker run --name qrcode -e a=$FILENAME -e b=$DATA -d yegekucuk2/qr-dockerize:$VERSION
echo "Successfully created docker image"

# Copy the file from the container to the Downloads directory
sleep 1
docker cp qrcode:/usr/src/app/$FILENAME.png ~/Downloads/$FILENAME.png

# Docker log
docker logs qrcode

# Delete the container after usage
docker rm -f qrcode
