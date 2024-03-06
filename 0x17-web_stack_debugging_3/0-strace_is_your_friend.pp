# 0-strace_is_your_friend.pp

package { 'strace':
  ensure => installed,
}

exec { 'strace_apache':
  command     => 'strace -o /tmp/strace_output.txt -p $(pidof apache2)',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}

exec { 'fix-wordpress':
  command     => 'echo "Fixing WordPress"',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  subscribe   => Exec['strace_apache'],
}

service { 'apache2':
  ensure    => running,
  subscribe => Exec['fix-wordpress'],
}
