FROM ruby:2.6.0

COPY rails-example-project .
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated nodejs 
RUN gem install bundler && \
    bundle install && \ 
    rails db:migrate

CMD rails s