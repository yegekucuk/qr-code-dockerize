# Python QR Code generator in Docker container

This Python QR Code generator application was made with use of Python and Docker technologies. It is very easy to use and creates a QR code png image in your `Downloads` folder.

## Installation and usage
1. Clone the repository
```bash
git clone https://github.com/yegekucuk/qr-code-dockerize.git
cd qr-code-dockerize
```
2. Run shell script with the usage `./run.sh <filename> <data>`. Your QR Code will be saved to `~/Downloads/<filename>.png`.
```bash
./run.sh <filename> <data>
```

## Clean up the image
The run.sh file creates a docker image when it is run. You can easily clean up the image with following command.
```bash
docker rmi yegekucuk2/qr-dockerize:latest
```

## Important note
It is a known bug that there can be only one word taken for both filename and data, so you can not put a sentence with seperate blanks on it. Example.
```bash
./run.sh filename HelloWorld! # Correct

./run.sh filename Hello World # Incorrect
./run.sh filename "Hello World" # Incorrect
./run.sh File Name HelloWorld! # Incorrect
./run.sh "File Name" HelloWorld! # Incorrect
```
