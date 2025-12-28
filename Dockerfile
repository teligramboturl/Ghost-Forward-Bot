FROM python:3.10.8-slim-buster
RUN apt install git -y
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Ghost-Forward-Bot
WORKDIR /Ghost-Forward-Bot
COPY . /Ghost-Forward-Bot
CMD gunicorn app:app & python3 main.py
