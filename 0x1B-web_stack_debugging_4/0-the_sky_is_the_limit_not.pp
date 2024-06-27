exec { 'increase_worker_processes':
  command => '/usr/sbin/nginx -s reload',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => 'grep -q "worker_processes 1;" /etc/nginx/nginx.conf',
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
}

file { '/etc/nginx/conf.d/optimization.conf':
  ensure  => file,
  content => template('nginx/optimization.conf.erb'),
}
