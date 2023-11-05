#!/bin/python
# Mars rover mission server

import socket
import marsWorld
import fileio
import rover
import _thread
import random
import time
import kryptera

world = marsWorld.Mars("../maps/LAN-map")

rovg1 = rover.Rover(4, 99, 0, world)
rovg2 = rover.Rover(6, 99, 1, world)
rovgl = rover.Rover(99, 99, 99, world)
marshen = rover.Rover(49, 2, -1, world)
world.printworldmap()

PIN1='6532'
PIN2='2840'
PIN3='9518'
PINL='6743'
PUK1='asdghfashd'
PUK2='jhfghjrjnf'
PUK3='mdjgwmkjhh'
PUKL='hmmmmmmmmm'
rovers = {PIN1:rovg1, PIN2:rovg2, PIN3:marshen, PINL:rovgl}
roverPINlist = {PUK1:PIN1,PUK2:PIN2,PUK3:PIN3, PUKL:PINL}

def com_loop(s):
    #takes commands and get correct rover to do stuff
    while(1):
        try:
            inp = s.recv(1024).decode('utf-8')
            rpin = inp[:4]

            if rpin == 'NWPN':
                rPUK = inp[4:]
                nPIN=changePIN(rPUK)
                s.send(nPIN.encode('utf-8'))
                continue
            else:
                rov = rovers[rpin]

            for n in range(4):
                try:
                    com = inp[4 + n]
                except:
                    print("to few arguments!")
                if (com == 'f'):
                    rov.moveForeward()
                elif (com == 'l'):
                    rov.rotate('l')
                elif (com == 'r'):
                    rov.rotate('r')
                elif (com == 'p'):
                    pstr = rov.getPosition()
                    s.send(pstr.encode('utf-8'))
                elif (com == 's'):
                    pstr = rov.getScan()
                    s.send(pstr.encode('utf-8'))
                elif (com == 'd'):
                    rov.drill()
                elif (com == 'l'):# read the 3 most reasent log lines
                    print("not done")
                    #TODO
                elif (com == 'L'): # read the whole log
                    for l in rov.readwholelog():
                        s.send(l.encode('utf-8'))
                    stop = "stop"
                    s.send(stop.encode('utf-8'))
#            elif (com == 'g'):
#                pstr = rov.getLog()
#                s.send(pstr.encode('utf-8'))
        except:
            s.close()
            print("closed")
            return



def changePIN(PUK):
# Makes sure that PINs are unique. Can also be used to initialize PIN-code => no delay
# lock mutex here
    delay=2*60 # in seconds
    roverPUKlist = {v: k for k, v in roverPINlist.iteritems()}
    newPIN=roverPINlist[PUK]
    while newPIN in roverPUKlist:
        newPIN = int(random.uniform(0, 10000))
        newPIN = str(newPIN)
        while len(newPIN)<4:
    	    newPIN = "0" + newPIN
        roverPINlist[PUK]=newPIN
    roverPINlist[PUK]=newPIN
    rovers[newPIN] = rovers.pop(oldPIN)
# Release mutex and wait unless init
    if oldPIN != "":
        time.sleep(delay)
    return newPIN

def adminTerminal(arg):
    print(arg)
    while(True):
        com = input(": ")

        if (com == "sm"):
            world.printworldmap()
        elif (com == "lr"):
            for pin, rover in rovers.items():
                print("Pin: " + pin + " rid: " + str(rover.rid) + " points: " + str(rover.score))
        elif (com == "cr"):
            print("under construction")
            kryptera.kryptera(roverPINlist, rovers)

def listening_loop(port):
    listener = socket.socket()
    host = socket.gethostname()
    listener.bind(('127.0.0.1', port))
    listener.listen(5)


    print("before")
    _thread.start_new_thread(adminTerminal, (0,))
    print("true")


    while True:
        client, addr = listener.accept()
        print("con")
        st = "connected"
        client.send(st.encode('utf-8'))
        _thread.start_new_thread( com_loop, (client, ) )


listening_loop(1200)

