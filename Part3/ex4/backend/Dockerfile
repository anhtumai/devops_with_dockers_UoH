FROM node

WORKDIR /home/node/app

COPY backend-example-docker /home/node/app

RUN chown -R node /home/node/app

USER node

RUN npm install

ENV FRONT_URL=http://localhost:5000

CMD npm start
