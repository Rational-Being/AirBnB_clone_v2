#puppet 

exec { 'update':
    command => '/usr/bin/env apt-get -y update'}

-> exec { 'nginx':
    command => '/usr/bin/env apt-get -y install nginx',
}

-> exec { 'release':
    command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}

-> exec { 'shared':
    command => '/usr/bin/env mkdir -p /data/web_static/shared/,
}

-> exec { 'fake content':
    command => '/usr/bin/env echo "fake content" | sudo tee /data/web_static/releases/test/index.html',
}

-> exec { 'ln':
    command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}

-> exec { 'chown':
    command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}

-> exec { 'nginx confg':
    command => '/usr/bin/env sed -i "/listen 80 default_server;/a location /hbnb_static/ {alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

-> exec { 'nginx':
    command => '/usr/bin/env service nginx restart',
}
