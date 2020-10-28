FROM ubuntu:16.04

WORKDIR /usr/src/app
COPY frontend-example-docker .
RUN apt-get update && apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash && \
    apt-get install -y nodejs && \
    node -v && npm -v && \
    apt-get purge -y --auto-remove curl && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    npm install

ENV API_URL=http://localhost:8000

CMD npm start
