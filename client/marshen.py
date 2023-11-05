#!/bin/python
# mars rover client
import socket
import time
import random

x = 0
y = 0
d = 'n'
pack = "9518"

def recive_message(addr, port):
    s = socket.socket()
    #host = socket.gethostbyaddr(addr.encode('UTF-8'))
    host = socket.gethostname()
    print(host)

    s.connect((addr , port))
    print(s.recv(1024).decode('utf-8'))
#    while(1):
#        st = input(": ")
#        s.send(st.encode('utf-8'))
#
#
#        for n in range(4):
#            if st[4 + n] == 'p':
#                print(s.recv(1024).decode('utf-8'))
#            elif st[4 + n] == 's':
#                scan = s.recv(1024).decode('utf-8')
#                print(scan[:5])
#                print(' ' + scan[5:])
#                print("  R")

    while(1):
        print("where am I")
        msg = pack + "p    "
        s.send(msg.encode('utf-8'))
        time.sleep(2)
        position = ''
        while True:
            try:
                position = s.recv(1024).decode('utf-8')
                break
            except:
                continue
        pos(position)

        rand = random.randint(0,7)
        print("time to move: " + str(rand))
        if rand == 0:
            msg = pack + move0()
        elif rand == 1:
            msg = pack + move1()
        elif rand == 2:
            msg = pack + move2()
        elif rand == 3:
            msg = pack + move3()
        elif rand == 4:
            msg = pack + move4()
        elif rand == 5:
            msg = pack + move5()
        elif rand == 6:
            msg = pack + move6()
        elif rand == 7:
            msg = pack + move7()
        s.send(msg.encode('utf-8')) 
        time.sleep(2)

        print("do I see anything?")
        i = 0
        while i < 4:
            i += 1
            msg = pack + "rs  "
            s.send(msg.encode('utf-8'))
            time.sleep(2)
            reseve = ""
            while True:
                try:
                    reseve = s.recv(1024).decode('utf-8')
                    break 
                except:
                    print("ERROR")
                    continue
            for ret in reseve:
                if ret == 'R':
                    msg = pack + 'rrff'
                    s.send(msg.encode('utf-8'))
                    msg = pack + 'ffff'
                    s.send(msg.encode('utf-8'))
                    break
        
        print("time to rest")
        time.sleep(4)

    s.close()


def pos(nyPos):
    pos = nyPos.split()
    x = pos[1]
    y = pos[3]
    d = pos[5]

def move0():
    if d == 'n':
        return 'f   '
    elif d == 'w':
        return 'rf  '
    elif d == 's':
        return 'rrf '
    elif d == 'e':
        return 'lf  '

def move1():
    if d == 'n':
        return 'frf '
    elif d == 'w':
        return 'rfrf'
    elif d == 's':
        return 'lflf'
    elif d == 'e':
        return 'flf '

def move2():
    if d == 'n':
        return 'rf  '
    elif d == 'w':
        return 'llf '
    elif d == 's':
        return 'lf  '
    elif d == 'e':
        return 'f   '

def move3():
    if d == 'n':
        return 'rfrf'
    elif d == 'w':
        return 'lflf'
    elif d == 's':
        return 'flf '
    elif d == 'e':
        return 'frf '

def move4():
    if d == 'n':
        return 'rrf '
    elif d == 'w':
        return 'lf  '
    elif d == 's':
        return 'f   '
    elif d == 'e':
        return 'rf  '

def move5():
    if d == 'n':
        return 'lflf'
    elif d == 'w':
        return 'flf '
    elif d == 's':
        return 'frf '
    elif d == 'e':
        return 'rfrf'

def move6():
    if d == 'n':
        return 'lf  '
    elif d == 'w':
        return 'f   '
    elif d == 's':
        return 'rf  '
    elif d == 'e':
        return 'rrf '

def move7():
    if d == 'n':
        return 'flf '
    elif d == 'w':
        return 'frf '
    elif d == 's':
        return 'rfrf'
    elif d == 'e':
        return 'lflf'

recive_message("127.0.0.1", 1200)
