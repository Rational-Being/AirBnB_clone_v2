#!/usr/bin/python3
"""
this script distributes an archive to my web servers
"""

from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['54.82.20.76', '100.26.161.177']

def do_deploy(archive_path):
    """
    this funtion performs te funtion in the comment above
    """
    if not exists(archive_path):
        return False
    try:
        compres = archive_path.split('/')[-1]
        new_path = '/data/web_static/releases/' + compres.strip('.tgz')
        put(archive_path, '/tmp')
        run('mkdir -p{}/'.format(new_path))
        run('tar -xzf /tmp/{} -C {}'.format(compres, new_path))
        run('rm /tmp/{}'.format(compres))
        run('mv {}/web_static/* {}'.format(new_path, new_path))
        run('rm -rf {}/web_static'.format(new_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(new_path))
        print('New version deployed')
        return True
    except Excception as e:
        return False