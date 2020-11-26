FROM alpine:latest

WORKDIR /usr/src

COPY main.sh .
# COPY inventory .

RUN touch inventory

RUN apk update &&\
    apk add git

RUN apk add --update docker openrc

RUN apk add --update bash && rm -rf /var/cache/apk/*

CMD [ "bash", "main.sh" ]
