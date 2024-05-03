#Using Puppet, install flask from pip3

#Installing flask from pip3 using Puppet
package {'flask':
  ensure   => installed,
  version  => '2.1.0',
  provider => pip3,
  require  => Package['python3.8'],
  require  => Package['python3-pip'],
}

#Ensuring that python present
package {'python3.8':
  ensure  => installed,
  version => '3.8.10',
}

#Ensuring that pip present
package { 'python3-pip':
  ensure => present,
}

#Installing Werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
}
