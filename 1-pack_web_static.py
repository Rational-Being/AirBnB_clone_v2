#!/usr/bin/python3
"""
this script will perform the funtion of do_pack
"""

from fabric.api import local
from datetime import date
from os import path


def do_pack():
    """
    a script that generate a .tgz archive form the contents of the folder
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
