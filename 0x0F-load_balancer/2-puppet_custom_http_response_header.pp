# This Puppet script configures Nginx to include a custom HTTP response header.

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Get the hostname of the server
$hostname = $::hostname

# Create a custom Nginx configuration file
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    add_header X-Served-By $hostname;

    location / {
        # Your existing configuration here
    }
}\n",
}

# Create a symbolic link to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
}

# Reload Nginx to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
