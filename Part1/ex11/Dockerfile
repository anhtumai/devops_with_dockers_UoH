FROM ubuntu:18.04

COPY backend-example-docker /backend-example-docker

WORKDIR /backend-example-docker

RUN apt update && apt install -y curl && curl -sL https://deb.nodesource.com/setup_10.x | bash && apt install -y nodejs
RUN node -v && npm -v

EXPOSE 8000

ENV FRONT_URL=http://localhost:5000

RUN npm install

CMD npm start