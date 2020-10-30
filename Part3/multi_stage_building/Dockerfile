FROM ruby as build-stage

WORKDIR /usr/app

RUN gem install jekyll
RUN jekyll new .
RUN jekyll build

FROM nginx

COPY --from=build-stage /usr/app/_site/ /usr/share/nginx/html