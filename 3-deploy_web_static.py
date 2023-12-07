#!/usr/bin/python3
"""
Code Deployment
"""
from os import path
from datetime import datetime
from fabric.api import local, run, put, env

env.hosts = ["54.86.225.115", "54.198.34.163"]


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


def do_deploy(archive_path):
    """distributes an archive to your web
    servers, using the function do_deploy"""
    if not path.exists(archive_path):
        return False

    file_name = path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    dest_path = "/data/web_static/releases/"
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}{}/".format(dest_path, folder_name))
        run("tar -xzf /tmp/{} -C {}{}/".
            format(file_name, dest_path, folder_name))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/".format(dest_path,
            folder_name, dest_path, folder_name))
        run("rm -rf {}{}/web_static".format(dest_path, folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".
            format(dest_path, folder_name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to web servers
    """
    path = do_pack()
    if not path:
        return False
    else:
        return do_deploy(path)
