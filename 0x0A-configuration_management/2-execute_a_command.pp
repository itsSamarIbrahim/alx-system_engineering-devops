#Using Puppet, create a manifest that kills a process named killmenow

exec {'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow',
  #path  => '/usr/bin/:/usr/local/bin/:/bin/'
  #or
  #command  => 'pkill killmenow',
  #provider => 'shell',
  #or
  #command => 'pkill -9 -f killmenow',
  #path    => ['/usr/bin', '/usr/sbin', '/bin']
}
