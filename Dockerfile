FROM python:latest
LABEL maintainer="alexfertel97@gmail.com"

COPY . /kojo

WORKDIR /kojo

VOLUME [ "/kojo/logs", "/kojo/results" ]

RUN pip install fire

ENTRYPOINT [ "python3", "main.py" ]