#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
Distributes an archive to your web servers, using the function do_deploy"""
import os
from fabric.api import *
from datetime import datetime


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    env.hosts = ['100.26.223.74', '54.237.53.61']

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

        return True
    except Exception as e:
        return False
