# ---------------------------------------------------------------------
# 
# File          : L00170171_Q5_File_2.py  
# Created       : 23/11/2021 13:59
# Author        : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   : Manipulate/Complete the following code to :
#                 1. install curl,
#                 2. Create a directory structure Labs with subfolders
#                    lab1 and lab2
#                 3. From your home directory find out when files were
#                    last accessed.
#
# ---------------------------------------------------------------------

import paramiko
import time
import re

# Open SSH connection to the device


def ssh_connection(ip):
    try:

        username = 'l00170171'
        password = 'lukasz123'

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()

        # First we need to update Ubuntu box before install Curl
        stdin, stdout, stderr = session.exec_command('echo lukasz123 | sudo -S apt-get update\n')

        output = ""

        for line in stdout:
            output = output + line
        if output != "":
            print(f"Ubuntu update:\n{output}")
        else:
            print("There was no output for this command")

        # Installation Curly
        stdin, stdout, stderr = session.exec_command('echo lukasz123 | sudo -S apt-get install -y curl\n')

        output = ""

        for line in stdout:
            output = output + line
        if output != "":
            print(f"Curl installed:\n{output}")
        else:
            print("There was no output for this command")

        # Creating new folders
        session.exec_command("mkdir Labs\n")  # Creating folder Lab
        session.exec_command("mkdir Labs/Lab1\n")  # Creating subfolder Lab1
        session.exec_command("mkdir Labs/Lab2\n")  # Creating subfolder Lab2

        # Showing created folder Labs
        stdin, stdout, stderr = session.exec_command('ls\n')

        output = ""

        for line in stdout:
            output = output + line
        if output != "":
            print(f"Folder Labs:\n{output}")
        else:
            print("There was no output for this command")

        # Showing created subfolders
        stdin, stdout, stderr = session.exec_command('ls ./Labs\n')

        output = ""

        for line in stdout:
            output = output + line
        if output != "":
            print(f"Labs subfolders:\n{output}")
        else:
            print("There was no output for this command")

        # File last accessed
        stdin, stdout, stderr = session.exec_command('ls -l --time=atime\n')

        output = ""

        for line in stdout:
            output = output + line
        if output != "":
            print(f"File last accessed:\n{output}")
        else:
            print("There was no output for this command")

        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print(f"There was at least one IOS syntax error on device {ip}")
        else:
            print(f"Commands successfully executed on {ip}")
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == "__main__":
    ssh_connection("192.168.178.122")
