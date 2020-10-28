FROM ruby:2.6.0

COPY rails-example-project /rails-example-project

WORKDIR /rails-example-project

RUN apt-get update && \
    apt-get install -y --allow-unauthenticated nodejs
RUN gem install bundler && \
    bundle install && \
    rails db:migrate

EXPOSE 3000

CMD rails s