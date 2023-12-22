file {'/tmp/school':
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  user    => 'www-data'
}
