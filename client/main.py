#!/bin/python
# mars rover client
import socket

def recive_message(addr, port):
    s = socket.socket()
    #host = socket.gethostbyaddr(addr.encode('UTF-8'))
    host = socket.gethostname()
    print(host)

    s.connect((addr , port))
    print(s.recv(1024).decode('utf-8'))
    #while(1):
        #st = input(": ")
        #s.send(st.encode('utf-8'))


        #for n in range(4):
            #if st[4 + n] == 'p':
            #    print(s.recv(1024).decode('utf-8'))
            #elif st[4 + n] == 's':
            #    scan = s.recv(1024).decode('utf-8')
            #    print(scan[:5])
            #    print(' ' + scan[5:])
            #    print("  R")
        #if st[:4] == "NWPN":
        #    print("nwpn")
        #    print(s.recv(1024).decode('utf-8'))
                

    while(1):
        pack = "6532"
        st = input(": ")
        #print(st)
        if st == 'w':
            pack += "fsp "
        elif st == 'a':
            pack += "lsp "
        elif st == 'd':
            pack += "rsp "
        elif st == 'e':
            pack += "d   "
        elif st == 'L':
            pack += "L   "

        #print("pack")
        #print(pack)
        s.send(pack.encode('utf-8'))
        


        for n in range(4):
            if pack[4 + n] == 'p':
                print(s.recv(1024).decode('utf-8'))
            elif pack[4 + n] == 's':
                scan = s.recv(1024).decode('utf-8')
                print(scan[:5])
                print(' ' + scan[5:])
                print("  R")
            elif pack[4 + n] == 'L':
                scan = str(s.recv(1024).decode('utf-8'))
                print(scan)
                while(str(scan[-4:]) != "stop"):
                    scan = s.recv(2048).decode('utf-8')
                    print(scan)




    s.close()

recive_message("127.0.0.1", 1200)
