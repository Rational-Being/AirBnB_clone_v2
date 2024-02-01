#!/usr/bin/python3

from fabric.api import local, put, run, env
from datetime import datetime
from os import path
from os.path import exists


def do_pack():
    """
    a script that generate archive for te files to be sent
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if not path.exists("versions"):
            local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz \
                web_static/".format(time))

        return "versions/web_static_{}.tgz".format(time)
    except Exception as e:
        return None


env.user = "ubuntu"
env.hosts = ["54.82.20.76", "100.26.161.177"]


def do_deploy(archive_path):
    """
    this is funtion has been described in 2-do_deploy_web_Static file
    """

    if not exists(archive_path):
        return False
    try:
        compres = archive_path.split("/")[-1]
        new_path = "/data/web_static/releases/" + compres.strip(".tgz")
        put(archive_path, "/tmp")
        run("mkdir -p{}/".format(new_path))
        run("tar -xzf /tmp/{} -C {}".format(compres, new_path))
        run("rm /tmp/{}".format(compres))
        run("mv {}/web_static/* {}".format(new_path, new_path))
        run("rm -rf {}/web_static".format(new_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_path))
        print("New version deployed")
        return True
    except Excception as e:
        return False


def deploy():
    """
    this funtion createsand sitributes an archive to my web servers
    """
    try:
        archive_path = do_pack()
    except Exception as e:
        return False

    return do_deploy(archive_path)
