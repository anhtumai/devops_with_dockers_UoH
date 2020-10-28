
FROM ubuntu:18.04

COPY frontend-example-docker /frontend-example-docker

WORKDIR /frontend-example-docker

RUN apt update && apt install -y curl && curl -sL https://deb.nodesource.com/setup_10.x | bash && apt install -y nodejs
RUN node -v && npm -v

EXPOSE 5000

RUN npm install

ENV API_URL=http://localhost:8000

CMD npm start