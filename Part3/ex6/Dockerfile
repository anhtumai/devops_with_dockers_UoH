FROM node:alpine as installer
COPY frontend-example-docker/package.json .
RUN npm install
########
FROM node:alpine as builder
COPY --from=installer /node_modules ./node_modules
COPY / .
RUN npm run build
########
FROM node:alpine as app
ENV NODE_ENV=production
WORKDIR /home/node/app
COPY --from=builder /dist ./dist
EXPOSE 5000
RUN npm install -g serve
CMD [ "serve", "-s", "dist" ]