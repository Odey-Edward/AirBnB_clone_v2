#!/usr/bin/env bash

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R "$USER":"$USER" /data

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

sudo service nginx reload
