FROM python:3.10.11

WORKDIR /data/

MAINTAINER Kanpon "kanpon@yeah.com.cn"

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

COPY ./main.py /code/main.py

#
RUN python main.py
