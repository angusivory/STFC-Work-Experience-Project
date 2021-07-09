FROM ubuntu:latest
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt -y install apache2
COPY ./resources/index.html /var/www/html/
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND
