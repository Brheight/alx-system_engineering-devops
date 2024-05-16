{ 'fix--for-nginx':
  command => "/bin/sed -i 's/worker_connections 768/worker_connections 1024/' /etc/nginx/nginx.conf && /bin/sed -i 's/keepalive_timeout 65/keepalive_timeout 75/' /etc/nginx/nginx.conf && service nginx reload",
}
