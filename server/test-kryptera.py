#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
from kryptera import kryptera
import socket
import marsWorld
import fileio
import rover
import _thread
import random
import time

#kryptera.debug=1

#def test( x ): return x*2
#x=4
#for i in range(3):
#	print test(x)

##PUK1 = '1akahfdakfh'
##PUK2 = '2akahfdakfh'
##PUK3 = '3akahfdakfh'
#PUK1 = 'R1'
#PUK2 = 'R2'
#PUK3 = 'R3'
#PIN1 = '1234'
#PIN2 = '4321'
#PIN3 = '5678'
#
#PIN1 = '0001'
#PIN2 = '0002'
#PIN3 = '0003'
##roverPINlist = {}
##roverPINlist[PUK1]=''
##roverPINlist[PUK2]=''
##roverPINlist[PUK3]=''
#roverPINlist = {PUK1:"",PUK2:"",PUK3:""}
#
#def changePIN(PUK):
## Makes sure that PINs are unique
## lock mutex here
#		maxpin=10000
#		delay=1
#		#maxpin=10
#		roverPUKlist = {v: k for k, v in roverPINlist.iteritems()}
#		oldPIN=newPIN=roverPINlist[PUK]
#		while newPIN in roverPUKlist:
#			newPIN = int(random.uniform(0, maxpin))
#			newPIN = str(newPIN)
#			while len(newPIN)<4:
#				newPIN = "0"+newPIN
#		roverPINlist[PUK]=newPIN
#		if oldPIN != "":
#		 	time.sleep(delay*60)
## Release mutex
#		return newPIN
#
#print changePIN(PUK1)
#print changePIN(PUK2)
#print changePIN(PUK3)
#print roverPINlist

PIN1='6532'
PIN2='2840'
PIN3='9518'
PUK1='asdghfashd'
PUK2='jhfghjrjnf'
PUK3='mdjgwmkjhh'
world = marsWorld.Mars("../LAN-map")
rovg1 = rover.Rover(2, 99, 0, world)
rovg2 = rover.Rover(4, 99, 1, world)
marshen = rover.Rover(49, 2, -1, world)
rovers = {PIN1:rovg1, PIN2:rovg2, PIN3:marshen}
roverPINlist = {PUK1:PIN1,PUK2:PIN2,PUK3:PIN3}

#test='abcdefgh'
#print test[4:]
print("==================================================")
for i in range(1):
	print("==================")
	print(kryptera(roverPINlist,rovers))

# vi: ts=2 sw=2 scs ai
