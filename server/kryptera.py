#!/usr/bin/python
# -*- coding: utf-8 -*-

def logKrypt(roverPINlist):
	out=kryptera(roverPINlist)
	for s in out:
		print(s)

def hexkryptering(string):
	output = ""
	s = ""
	string = string.upper()
	#print "ASCII value: ", ', '.join(str(ord(c)) for c in string)
	for i in string:
		output += i.encode("hex")
	return output

def matriskryptering(str):
	UC = 'SPACE'
	LC = UC.lower()
	strs = 'abcdefghijklmnoprstuvwxyz'
	lista = []
	conv = {}
	output = ""
	lista = list(strs)
	#print lista
	i = 0
	for U in UC:
		for L in LC:
			conv[lista[i]] = U+L
			i+=1
	#print conv
	for i in str:
		output += conv[i]
	return output

def shifttextkryptering(shift,str):
	strs = 'abcdefghijklmnopqrstuvwxyz'
	data = []
	for i in str:                     #iterate over the text
		if i.strip() and i in strs:                 # if the char is not a space ""  
			data.append(strs[(strs.index(i) + shift) % 26])    
		else:
			data.append(i)           #if space the simply append it to data
	output = ''.join(data)
	return output

def kryptera( roverPINlist, rovers ):
	u"""Kryptera och skicka tillbaks, ska sedan läggas till respektive rover-log"""
	if kryptera.debug: print(roverPINlist)
	typ = (kryptera.order % 3)
	if kryptera.debug: print("Order: ",kryptera.order," typ: ",typ," hint: ",kryptera.hint)

	# Kryptera koder
	numberlist = {}
	numberlist[0] = "zero"
	numberlist[1] = "one"
	numberlist[2] = "two"
	numberlist[3] = "three"
	numberlist[4] = "four"
	numberlist[5] = "five"
	numberlist[6] = "six"
	numberlist[7] = "seven"
	numberlist[8] = "eight"
	numberlist[9] = "nine"
	encryptedlist = {}
	for PUK, PIN in roverPINlist.items():
		kod = list(PIN)
		if kryptera.debug: print(kod)
		str = ''
		for c in kod[0:3]: str+=numberlist[int(c)]
		if kryptera.debug: print(str)
		if typ == 0:
			encrypted = shifttextkryptering(kryptera.order+1,str)
		if typ == 1:
			encrypted = hexkryptering(str)
		if typ == 2:
			encrypted = matriskryptering(str)
		if kryptera.debug: print(encrypted)
		encryptedlist[PUK] = encrypted
	if kryptera.debug: print(encryptedlist)

	# Ge tips halvvägs
	msg = 'Vi har lyckats komma över den första delen av säkerhetskoden till ett konkurrerande företag i krypterat format: '
	msg2 = ''
	if kryptera.hint:
		if typ == 0: msg2 = ". Vi tror att det är någon typ av cesarchiffer..."
		if typ == 1: msg2 = ". Vi tror att det är någon typ av asciichiffer..."
		if typ == 2: msg2 = ". Vi tror att det är någon typ av matrischiffer som har med rymden att göra..."

	# Fördela krypterade koder
	i=0
	returnmsg = {}
	PUKlist= list(roverPINlist.keys())
	for PUK in PUKlist:
		if kryptera.debug: print(PUK,i)
		new=(i+int(kryptera.order)+1+int(kryptera.order/3)) % len(PUKlist)
		if new == i: new+=1
		new = new % len(PUKlist)
		newPUK=PUKlist[new]
		if kryptera.debug: print("FROM: ",PUK,"->",newPUK,"i:",i,"->",new)
		returnmsg[newPUK] = msg+encryptedlist[PUK]+msg2
		i+=1

	if kryptera.hint: kryptera.order+=1
	kryptera.hint ^= 1 
	for PUK,msg in returnmsg.items():
		obj = rovers[roverPINlist[PUK]]
		obj.log.write('k', msg, 0)
	return returnmsg

kryptera.order=0
kryptera.hint=0
kryptera.debug=0

# vi: ts=2 sw=2 scs ai
