# ---------------------------------------------------------------------
# 
# File          : L00170171_Q4_File_2.py
# Created       : 22/11/2021 10:28
# Author        : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   :Determine which ports are open
#
# ---------------------------------------------------------------------

import socket
import subprocess
import sys
import re
from datetime import datetime


def port_scan():
    """
    This function will scan ports
    """

    # Clear the screen
    subprocess.call('clear', shell=True)

    # Ask for input
    remote_server = input('Enter remote host to scan: ')
    remote_server_ip = socket.gethostbyname(remote_server)



    # Print a nice banner with information on which host we are about to scan
    print(" ")
    print("-" * 60)
    print("Please wait, scanning remote host", remote_server_ip)
    print("-" * 60)
    print(" ")

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify port (here it will scan ports between 1 and 1024)
    # We also put in some error handling for catching errors

    try:
        # try 1, 1025 if you have time
        for port in range(1, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip, port))

            if port == 22:
                print(f'SSH:  {port}    Open')
            elif port == 80:
                print(f'HTTP: {port}    Open')
            elif result == 0:
                print(f'Port {port}:   Open')
            sock.close()

    except KeyboardInterrupt:
        print('You pressed Ctrl+C')
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    # Print a nice banner with information on which host we are about to scan
    print(" ")
    print("-" * 60)
    print('Scanning Completed in: ', total)
    print("-" * 60)


if __name__ == "__main__":
    port_scan()
