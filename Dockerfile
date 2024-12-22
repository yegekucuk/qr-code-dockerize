# Dockerfile image creation
FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["/bin/sh", "-c", "python qr/main.py $a $b"]
