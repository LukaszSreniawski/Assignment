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
import re

# You can scan 0-65535 ports.
port_min = 0
port_max = 90

# Ask user to input the ip address they want to scan.
while True:
    ip = input("\nPlease enter the ip address that you want to scan: ")
    break

open_ports = []

# Socket port scanning
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            open_ports.append(port)
    except:
        pass

# showing open ports
for port in open_ports:
    if port == 22:
        print(f"SSH: port {port} is open on ip: {ip}.")
    elif port == 80:
        print(f"HTTP: port {port} is open on ip: {ip}.")
