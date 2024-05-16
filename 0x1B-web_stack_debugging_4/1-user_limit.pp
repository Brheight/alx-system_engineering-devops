{ 'change-os-configuration-for-holberton-user':
  command => "/bin/echo 'holberton soft nofile 65536' >> /etc/security/limits.conf && /bin/echo 'holberton hard nofile 65536' >> /etc/security/limits.conf && /bin/echo 'session required pam_limits.so' >> /etc/pam.d/common-session",
  unless  => "grep -q 'holberton' /etc/security/limits.conf",
}
