# ---------------------------------------------------------------------
# 
# File          : q_3.py  
# Created       : 14/11/2021 08:27
# Author        : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   : Connect to the virtual machine using a python script using the ssh
#
# ---------------------------------------------------------------------

import paramiko
import sys

results = []

def ssh_conn():
    ip = '192.168.178.122'
    username = 'l00170171'
    password = 'lukasz123'

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(ip, username=username, password=password)

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('systemctl status ssh')

    for line in ssh_stdout:
        results.append(line.strip('\n'))

    print("connected to: ", ip)


ssh_conn()

for i in results:
    print(i.strip())


sys.exit()
