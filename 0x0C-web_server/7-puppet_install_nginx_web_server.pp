#!/usr/bin/env puppet
# Puppet manifest to install and configure Nginx server with a 301 redirect.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create a custom HTML page with "Hello World!"
file { '/usr/share/nginx/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80 and serve the custom HTML page
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80;
    server_name localhost;

    location /redirect_me {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}",
  require => Package['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [File['/etc/nginx/sites-available/default'], File['/usr/share/nginx/html/index.html']],
}

# Notify to reload Nginx when the configuration changes
exec { 'reload_nginx':
  command     => '/bin/kill -s HUP $(/bin/pgrep -f "nginx: master process")',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
