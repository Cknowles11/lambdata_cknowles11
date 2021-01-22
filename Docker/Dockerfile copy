FROM debian

ENV PYTHONUNBUFFERED=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV SHELL=/bin/bash


RUN apt-get update && \ 
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv


RUN pip3 install pandas

RUN pip3 install -i https://test.pypi.org/simple/ help-func