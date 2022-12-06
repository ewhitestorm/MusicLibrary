FROM python:3.9.5-alpine
WORKDIR /usr/src/app/
COPY requirements.txt ./
RUN pip install -r requirements.txt
LABEL maintainer="https://github.com/ewhitestorm"