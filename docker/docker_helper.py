"""
Docker Helper
Assists with Docker administration.
"""

import subprocess
import sys
import argparse

def get_container_ip_addrs():
    """
    Retrieves the IP addresses associated with each container.
    Prints to stdout when complete.
    """
    try:
        pcs = subprocess.Popen("docker exec -i -t $(docker ps -l -q) \
                               ip addr sho", stdout=PIPE)
        print(pcs.communicate())
    except subprocess.CalledProcessError:
        sys.exit(1)

def rm_exited_addrs():
    """
    Culls unnecessary Docker containers. Prints to stdout when complete.
    Adapted from @FiloSottile's original command.
    """
    try:
        pcs = subprocess.Popen("docker ps -a | egrep -i \"exit|created\" \
                               | cut -d ' ' -f 1 | xargs sudo docker rm", \
                               stdout=PIPE)
        print(pcs.communicate())
    except subprocess.CalledProcessError:
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('get-container-ips', \
                        dest='get_container_ip_addrs' \
                        help='Fetches container IP addresses.')
    parser.add_argument('cull-exited-containers', \
                        dest='rm_exited_addrs' \
                        help='Culls unnecessary containers.')
    parser.add_argument(description='CLI-based Docker helper', \
                        help='Created by james-daniel.')
    for arg in vars(parser):
        print(arg)