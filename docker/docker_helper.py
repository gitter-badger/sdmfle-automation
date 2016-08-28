"""
Docker Helper
Author: James Daniel
Purpose: Centralized Docker program to assist with automating common tasks.
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
        subprocess.call("docker exec -i -t $(docker ps -l -q) \
                               ip addr sho", shell=True)
    except subprocess.CalledProcessError:
        sys.exit(1)

def rm_exited_addrs():
    """
    Culls unnecessary Docker containers. Prints to stdout when complete.
    Adapted from @FiloSottile's original command.
    """
    try:
        subprocess.Popen("docker ps -a | egrep -i \"exit|created\" \
                               | cut -d ' ' -f 1 | xargs docker rm", \
                               shell=True)
    except subprocess.CalledProcessError:
        sys.exit(1)

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--get-container-ips', \
                        dest='get_container_ip_addrs', \
                        help='Fetches container IP addresses.')
    PARSER.add_argument('--cull-exited-containers', \
                        dest='rm_exited_addrs', \
                        help='Culls unnecessary containers.')
    PARSER.print_help()
    