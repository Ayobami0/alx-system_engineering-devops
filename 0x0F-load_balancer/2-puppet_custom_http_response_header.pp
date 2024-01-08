file {'/etc/nginx/nginx.conf':
  ensure  => present,
  content => "
http {
			server {
							listen 80;
							root /var/www/data/;
							index index.html;
							error_page 404 /404.html;
							add_header X-Served-By \$hostname;
							location /redirect_me {
											rewrite ^/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
							}
							location /404.html {
											root /var/www/data/error;
											internal;
							}
			}
}
events {}",
  require => Package['nginx']
}


file {'/var/www/data/index.html':
  ensure  => present,
  content => "Hello World!\n",
  require => File['/etc/nginx/nginx.conf']
}

file {'/var/www/data/error/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n"
  require => File['/var/www/data/index.html']
}

service {'nginx':
  ensure  => running,
  require => File['/var/www/data/error/404.html']
}

exec {'sudo su; sudo apt-get update':
  before => Package['nginx']
}

package {'nginx':
  ensure          => installed,
  provider        => apt,
  install_options => ['-y'],
}
