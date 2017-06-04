#!/usr/bin/python
import time,commands

commands.getoutput('systemctl start rpcbind')
commands.getoutput('yum install nfs-utils rpcbind -y')
commands.getoutput('mkdir /media/kkda')
commands.getoutput('mount -t nfs 192.168.1.100:/mnt/kkda /media/kkda')
commands.getoutput('iptables -F')
commands.getoutput('setenforce 0')