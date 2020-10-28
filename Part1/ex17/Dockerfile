FROM alpine
LABEL maintainer="emaitux"

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /project

CMD pip3 install -r requirement.txt && python3 main.py