#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file = 'versions/web_static_' + timestamp + '.tgz'
    local("mkdir versions")
    result = local(f"tar -cvzf {file} web_static")
    if result.succeeded:
        return file
    else:
        return
