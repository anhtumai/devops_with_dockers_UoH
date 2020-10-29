FROM ubuntu:16.04

ENV LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y \
    curl python ca-certificates && \
    curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
    chmod a+x /usr/local/bin/youtube-dl && \
    apt-get purge -y --auto-remove curl && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m app

USER app

WORKDIR /app

ENTRYPOINT ["/usr/local/bin/youtube-dl"]