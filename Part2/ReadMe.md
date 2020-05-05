## Part 2 

### Docker compose 

Compose is a tool for defining and running multi-container Docker applications
- Multiple isolated environments on a single host 
- Preserve volume data when containers are created 
- Only recreate containers that have changed 
- Variables and moving a composition between environments 

In short, Compose enables running __multiple containers__ with a __single__ command. 


__Note__: LC_ALL: force all application use default language for output (English)


### 2.1 

[Docker Compose file](./ex1/docker-compose.yml)

```
$> cd ex1
$> touch app/logs.txt # this is important, since docker-compose will think logs.txt is a directory by default
$> docker-compose up
```
![](./2-1.png)

### 2.2 

[Docker Compose file](./ex2/docker-compose.yml)
```
$> cd ex2
$> docker-compose up -d
$> curl localhost:8000
Ports configured correctly!!
```

![](2-2.png)

### 2.3

[Docker Compose file](./ex3/docker-compose.yml)

```
# Go to part 1
$> docker build -t frontend ex110
$> docker build -t backend ex111
$> docker-compose up
```

### 2.4

[Docker Compose file](./scaling-exercise/docker-compose.yml)

```
$> docker-compose up --scale compute=2
```

![](2-4.png)

### 2.5

[Project](./ex5/docker-compose.yml)
[Backend Dockerfile](./ex5/backend/Dockerfile)
```
$> docker-compose up
```
![](2-5.png)

### 2.6

[Project](./ex6/docker-compose.yml)
```
$> docker-compose up
```

### 2.7