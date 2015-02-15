import os

from fabric.api import local, cd, run, env


env.hosts = ['root@104.236.173.149']
env.key_filename = '/Users/cai/.ssh/id_rsa.pub'


def local_operation(commit_msg):
    print("local~ ")
    local_path = os.path.dirname(__file__)
    with cd(local_path):
        local('git add .')
        local('git commit -am "%s"' % (commit_msg))
        local('git push origin hotfix:hotfix')


def remote_operation(commit_msg):
    print("Remote ~")
    with cd("/root/xiascrobble"):
        run('git pull origin hotfix -m "%s"' % (commit_msg))


def oper(commit_msg):
    local_operation(commit_msg)
    remote_operation(commit_msg)
