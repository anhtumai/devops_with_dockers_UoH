FROM node

WORKDIR /usr/src/app  

COPY frontend-example-docker frontend-example-docker 
RUN cd frontend-example-docker && npm install 
ENV API_URL=http://localhost:8000

CMD cd frontend-example-docker && npm start 