FROM node

WORKDIR /usr/src/app  

COPY backend-example-docker backend-example-docker 
RUN cd backend-example-docker && npm install 
ENV FRONT_URL=http://localhost:5000 REDIS=localhost REDIS_PORT=6379

CMD cd backend-example-docker && npm start 