#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    archive and compress the web_static directory
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)

    local("mkdir -p versions")
    path = "versions/{}".format(name)
    result = local("tar -czvf {} web_static".format(path))

    if result.failed:
        return (None)
    else:
        return (path)
