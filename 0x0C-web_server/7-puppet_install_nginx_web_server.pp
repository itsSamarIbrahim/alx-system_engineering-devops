# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure          => installed,
  require         => Exec['update system'],
  install_options => ['-y'],
}

file_line { 'install':
  ensure => 'presesnt',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/itssamaribrahim permanent;',
}

file { 'Home page':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  mode    => '0744',
  owner   => 'www-data',
  content => 'Hello World!',
  require => Exec['nginx'],
}

file { '404 page':
  ensure  => 'file',
  path    => '/var/www/error/404.html',
  mode    => '0744',
  owner   => 'www-data',
  content => "Ceci n'est pas une page\n",
  require => Exec['nginx'],
}

exec { 'Restart nginx':
  command => 'service nginx restart',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

exec { 'run':
  command  => 'sudo service nginx restart',
}
