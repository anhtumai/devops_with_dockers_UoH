FROM node:15.0.1-alpine3.10

WORKDIR /backend-example-docker

COPY backend-example-docker /backend-example-docker

RUN chown -R node /backend-example-docker

USER node

RUN npm install

ENV FRONT_URL=http://localhost:5000

CMD npm start
