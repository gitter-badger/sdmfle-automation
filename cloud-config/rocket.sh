#!/bin/bash

scp -i /home/jdaniel/.ssh/id_rsa.pub /home/jdaniel/git-securitydaemons/sdmfle-conf/coreos/cloud-config/cloud-config_n0.yml core@10.5.5.12:~/
scp -i /home/jdaniel/.ssh/id_rsa.pub /home/jdaniel/git-securitydaemons/sdmfle-conf/coreos/cloud-config/cloud-config_n1.yml core@10.5.5.13:~/
scp -i /home/jdaniel/.ssh/id_rsa.pub /home/jdaniel/git-securitydaemons/sdmfle-conf/coreos/cloud-config/cloud-config_n2.yml core@10.5.5.14:~/
scp -i /home/jdaniel/.ssh/id_rsa.pub /home/jdaniel/git-securitydaemons/sdmfle-conf/coreos/cloud-config/cloud-config_n3.yml core@10.5.5.15:~/