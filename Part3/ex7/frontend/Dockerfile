FROM node:15.0.1-alpine3.10 AS installer

WORKDIR /frontend-example-docker

COPY frontend-example-docker /frontend-example-docker

RUN chown -R node /frontend-example-docker

USER node

RUN npm install && npm build


FROM node:15.0.1-alpine3.10

USER node

COPY --from=installer /frontend-example-docker /home/node

WORKDIR /home/node

EXPOSE 5000

ENV API_URL=http://localhost:8000

CMD npm start
