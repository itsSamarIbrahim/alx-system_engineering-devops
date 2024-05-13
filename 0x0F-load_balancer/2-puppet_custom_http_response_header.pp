# automate the task of creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

exec { 'custom HTTP header response':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/server_name _/s/$/\n\tadd_header X-Served-By $HOSTNAME;/" /etc/nginx/sites-enabled/default;
  sudo nginx -t;
  sudo service nginx restart',
  provider => shell,
}
