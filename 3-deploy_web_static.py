#!/usr/bin/python3
"""
Code Deployment
"""
from os import path, stat
from datetime import datetime
from fabric.api import local, run, put, env, runs_once

env.hosts = ["54.86.225.115", "54.198.34.163"]


@runs_once
def do_pack():
    """
    archive and compress the web_static directory
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)

    path = "versions/{}".format(name)
    print("Packing web_static to {}".format(path))
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(path))
    archize_size = stat(path).st_size
    print("web_static packed: {} -> {}Bytes".format(path, archize_size))

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
    result = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}{}/".format(dest_path, folder_name))
        run("tar -xzf /tmp/{} -C {}{}/".
            format(file_name, dest_path, folder_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/".format(dest_path,
            folder_name, dest_path, folder_name))
        run("rm -rf {}{}/web_static".format(dest_path, folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".
            format(dest_path, folder_name))
        print("New version deployed!")
        result = True
    except Exception:
        result = False

    return result


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
