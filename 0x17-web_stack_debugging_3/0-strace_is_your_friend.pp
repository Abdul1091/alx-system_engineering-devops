# Puppet manifest to fix a 500 error
# Fix the mistyped file extension in wp-settings.php

exec { 'fix-wordpress-server-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
  notify  => Service['apache2'],
}
