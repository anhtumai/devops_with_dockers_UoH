# Part 2

## Docker compose

Compose is a tool for defining and running multi-container Docker applications

- Multiple isolated environments on a single host
- Preserve volume data when containers are created
- Only recreate containers that have changed
- Variables and moving a composition between environments

In short, Compose enables running **multiple containers** on a **single host** with a **single** command. To use with **multiple host**, Ks8 is the way to go.

Normally, Docker containers run in **isolation** but Docker Compose finds a way to make them **communicate**.

All Docker Compose files are **YAML** files.

Example: A big website need to call to **multiple** applications

**Note**: LC_ALL: force all application use default language for output (English)

Basic commands:

- docker-compose up: create and start containers
- docker-compose down: stop and remove containers,
  networks, images, volumes.

- docker-compose build: build/rebuild services.
  (Service is a group of at least 1 containers)

To understand docker-compose file, it is essential to understand the command line arguments
of docker run first.

```yaml
services:
    <image name>:
        image: <image name>
        build: <build folder (containg the image)>
            ( = docker build <build folder>)
        ports:
            - host_port:container_port
            ( = docker run -p)
        volumes:
            - host_path:container_path
            (host_path can be relative path)
            ( = docker run -v)
        environments:
            - <container_ENV_var>=<value>
            ( = docker run -e)
```

### Reverse Proxy

a, Proxy

A proxy acts as a gateway between you and the Internet.

> Your computer makes a request to a web server. In this case, a proxy acts as a medium between you and the server, making a request **on your behalf**. There are some benefits:
>
> - data security (the request will use proxy IP address, firewall,filter, ... )
> - cache data improve performance

b, Reverse Proxy

Reverse Proxy is not used by the client, but is used by **server admins**. It intercepts requests from clients, send and receive responses from the origin server.

<img src="https://www.cloudflare.com/img/learning/cdn/glossary/reverse-proxy/reverse-proxy-flow.svg" style="background-color:white" >

<!-- ![Reverse Proxy](https://www.cloudflare.com/img/learning/cdn/glossary/reverse-proxy/reverse-proxy-flow.svg) -->

Why reverse proxy:

- Load balancing: Provide solution to handle millions of requests per day.
- Protection from attack
- Global Server Load Balancing
- Caching: this concept is intertwined with CDN. To load a Youtube video from Helsinki, it is highly likely that your laptop gets data from a reverse proxy/CDN in Europe instead of
- TLS encryption

## Exercises

### 2.1

[Docker Compose file](./ex1/docker-compose.yml)

```shell
$> cd ex1
$> touch app/logs.txt # this is important, since docker-compose will think logs.txt is a directory by default
$> docker-compose up
```

![2.1](./2-1.png)

### 2.2

[Docker Compose file](./ex2/docker-compose.yml)

```shell
$> cd ex2
$> docker-compose up -d
$> curl localhost:8000
Ports configured correctly!!
```

![2.2](2-2.png)

### 2.3

[Docker Compose file](./ex3/docker-compose.yml)

```yaml
version: "3.5"

services:
  frontend:
    ports:
      - 5000:5000
    build: ../../Part1/ex110
  backend:
    ports:
      - 8000:8000
    build: ../../Part1/ex111
    volumes:
      - ./logs.txt:/backend-example-docker/logs.txt
```

### 2.4

[Docker Compose file](./scaling-exercise/docker-compose.yml)

```shell
$> docker-compose up --scale compute=2
```

![2.4](2-4.png)

### 2.5

[Docker Compose file](./ex5/docker-compose.yml)

```yaml
version: "3"
services:
  frontend:
    build: ./frontend
    image: frontend
    ports:
      - 5000:5000

  backend:
    build: ./backend
    image: backend
    ports:
      - 8000:8000
    environment:
      - REDIS=redis
      - REDIS_PORT=6379
  redis:
    image: redis:alpine
    ports:
      - 6379:6379
```

![2.5](2-5.png)

### 2.6

[Docker-compose file](./ex6/docker-compose.yml)

```yaml
database:
  image: postgres
  restart: always
  environment:
    - POSTGRES_PASSWORD=password
    - POSTGRES_USER=anhtumai
```

**Note**: After some experimenting, backend and database connection doesnot work with `FROM node`, so I change Docker file in backend and frontend service to `FROM ubuntu:18.04`.

![2.6](2-6.png)

### 2.7

Skipped

### 2.8

[Docker-compose file](./ex8/docker-compose.yml)

```yaml
proxy:
  depends_on:
    - frontend
    - backend
  restart: always
  image: nginx:alpine
  ports:
    - 8080:80

  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
```

![2.8](2-8.png)

### 2.9

[Docker-compose file](./ex9/docker-compose.yml)

```yaml
database:
  image: postgres
  restart: always
  environment:
    - POSTGRES_PASSWORD=password
    - POSTGRES_USER=anhtumai
  volumes:
    - ./database:/var/lib/postgresql/data
```

```shell
$> sudo su
$> docker-compose up -d
$> docker-compose down
$> rm -R database
$> docker-compose up -d
```

![2.9](2-9.png)

### 2.10

First, copy the docker-compose.yml in ex8. You need to remove `ENV API_URL ...` in frontend [Dockerfile](./ex10/frontend/Dockerfile). In [docker-compose.yml](./ex10/docker-compose.yml), add:

```yaml
frontend:
  ports:
    - 5000:5000
  build: frontend
  environment:
    - API_URL=http://localhost:8080/api
```

![2.10](2-10.png)
