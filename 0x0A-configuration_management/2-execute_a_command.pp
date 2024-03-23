#Creating a manifest that kills a process named killmenow using Puppet

exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => shell,
}
