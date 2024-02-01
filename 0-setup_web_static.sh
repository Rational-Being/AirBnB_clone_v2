#!/usr/bin/env bash
#

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
sudo cat >> /data/web_static/releases/test/index.html << EOF

<html>
<head>
</head>
<body>
    Fake Content
</body>
</html>

EOF

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed -i "/listen 80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart