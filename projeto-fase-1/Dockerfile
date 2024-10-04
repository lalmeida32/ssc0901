FROM php:5.6-apache

RUN docker-php-ext-install mysql mysqli pdo pdo_mysql

COPY ./sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y mysql-client

COPY ./site /var/www/html/

EXPOSE 80