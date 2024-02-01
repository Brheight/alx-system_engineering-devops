# This Puppet manifest configures the SSH client to use the private key and refuse password authentication

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
