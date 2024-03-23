#Installing flask from pip3 using Puppet

# ensure that python present
package { 'python3.8':
  ensure => present,
}

# ensure that pip present
package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
