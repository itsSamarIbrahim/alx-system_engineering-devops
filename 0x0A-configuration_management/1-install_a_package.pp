#Using Puppet, install flask from pip3

#Ensuring that python present
package { 'python3.8':
  ensure => present,
}

#Ensuring that pip present
package { 'python3-pip':
  ensure => present,
}

#Installing flask from pip3 using Puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}

#Installing Werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
}
