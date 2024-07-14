#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['100.26.223.74', '54.237.53.61']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/alx_key'


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

    if not archive_path or not os.path.isfile(archive_path):
        return False

    try:
        file = archive_path.split('/')[-1]
        file_no_ext = file.split('.')[0]
        releases = "/data/web_static/releases"
        extract_path = f"{releases}/{file_no_ext}"

        put(archive_path, f"/tmp/{file}")

        run(f"mkdir -p {extract_path}")

        run(f"tar -xzf /tmp/{file} -C {extract_path}")

        run(f"rm /tmp/{file}")

        run(f"mv {extract_path}/web_static/* {extract_path}")

        run(f"rm -rf {extract_path}/web_static")

        run("rm -rf /data/web_static/current")

        run(f"ln -s {extract_path} /data/web_static/current")

        if run(f"test -f /data/web_static/current/0-index.html").failed:
            print("Missing /data/web_static/current/0-index.html")
            return False

        return True
    except Exception as e:
        return False


def deploy():
    """Calls the do_pack() and do_deploy() functions in succession"""

    archive = do_pack()
    if not archive:
        return False
    return do_deploy()
