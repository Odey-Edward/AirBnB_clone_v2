#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

echo "server {
   listen 80 default_server;
   listen [::]:80 default_server;

   root /var/www/html;
   index index.html;

   location / {
        add_header X-Served-By $HOSTNAME;
   }
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }

   location /hbnb_static/ {
        alias /data/web_static/current/;
   }

   error_page 404 /404.html;
   location = /404.html{
      internal;
   }

}" > /etc/nginx/sites-available/default

sudo service nginx restart
