FROM openjdk:8-slim

COPY spring-example-project spring-example-project 

RUN cd spring-example-project && ./mvnw package
CMD cd spring-example-project && java -jar ./target/docker-example-1.1.3.jar
