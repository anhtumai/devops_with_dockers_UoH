FROM node:15.0.1-alpine3.10 AS installer

WORKDIR /frontend-example-docker

COPY frontend-example-docker /frontend-example-docker

RUN npm install && npm run build

FROM node:15.0.1-alpine3.10

COPY --from=installer /frontend-example-docker/dist /dist

RUN npm install -g serve

CMD serve -s -l 5000 dist
