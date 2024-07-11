#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static

# Update package lists on ubuntu based systems
sudo apt update

# Install nginx web server
sudo apt install -y nginx

# Create document directories:
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Dummy html file to test Nginx configuration
sudo echo "<h1>Hello World!</h1>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Symbolic link of `/data/web_static/releases/test`
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Changing ownership of `/data/` directory to `ubuntu` user/group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i "/server_name _;/a\\
	location /hbnb_static {\\
		alias /data/web_static/current/;\\
		autoindex off;\\
	}\\
" /etc/nginx/sites-available/default

# Update configuration
sudo service nginx restart
