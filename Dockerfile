FROM ubuntu:23.04

WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get upgrade -y
RUN apt-get install -y nginx curl python3 python3-distutils python3-apt

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

COPY src/ .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 4040

ARG debugMode

ENV debugMode=$debugMode
