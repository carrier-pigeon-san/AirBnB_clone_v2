#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
Distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file = 'versions/web_static_' + timestamp + '.tgz'
    local("mkdir -p versions")
    result = local(f"tar -cvzf {file} web_static")
    if result.succeeded:
        return file
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    env.hosts = ['100.26.223.74', '54.237.53.61']
    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/alx_key'
    if archive_path:
        releases = "/data/web_static/releases"
        file = archive_path.split('/')[-1].split('.')[0]
        result = local(f"ls {archive_path}")
        if result.succeeded:
            try:
                put(archive_path, "/tmp/")
                sudo(f"tar -xzvf /tmp/{archive_path} -C {releases}/{file}")
                sudo(f"rm -rf /tmp/{archive_path.split('/')[0]}")
                sudo(f"ln -sf {releases}/{file} /data/web_static/current")
                return True
            except Exception as e:
                pass
    return False
