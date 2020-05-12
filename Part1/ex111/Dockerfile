FROM ubuntu:18.04

WORKDIR /
COPY backend-example-docker backend-example-docker
RUN apt update && apt install -y curl && curl -sL https://deb.nodesource.com/setup_10.x | bash && apt install -y nodejs
RUN node -v && npm -v

ENV FRONT_URL=http://localhost:5000
CMD cd backend-example-docker && npm install && npm start