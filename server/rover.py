# rover class

import marsWorld
import logger
import random
from threading import Lock
import time

class Rover:
    rid = 0
    def __init__(self, x, y, color, world):
        self.rovLock = Lock()
        self.rid = Rover.rid
        Rover.rid = Rover.rid + 1
        self.x = x
        self.y = y
        self.on = False
        self.newmessage = False
        self.color = color
        self.direction = 'n'
        self.world = world
        self.under = self.world.getPoint(self.x, self.y)
        self.world.putOnWorldMap(self.x, self.y, self)
        self.score = 0
        
        self.lastPush = self.rid
        self.lastDrill = self.rid
        # 104 x 104 x 2
        # the surandig wals need to be considerd.
        # [][][explored, driled]
        self.mapStat = [[[False for i in range(2)] for j in range(104)] for k in range(104)]
        self.data = [False, False]

        self.log = logger.Logger(self.rid, self.color)

    def __str__(self):
        if self.color == -1:
            return 'M'
        return 'R'

    def getxydir(self):
        return self.x, self.y, self.direction

    def getPosition(self):
        self.rovLock.acquire()
        time.sleep(0.5)
        x, y, direction = self.getxydir()
        anser = "x: " + str(x) + " y: " + str(y) + " direction: " + str(direction)
        self.log.write('p', anser, self.score)
        self.rovLock.release()
        return anser

    def readwholelog(self):
        self.rovLock.acquire()
        time.sleep(0.5)
        logen = self.log.readLog()
        self.rovLock.release()
        return logen

#             1             5
#  12345     62      R      48
#   678     R73     876     37R
#    R       84    54321    26
#             5             1

    def getScan(self):
        ret = ""
        self.rovLock.acquire()
        time.sleep(0.5)
        self.world.worldLock.acquire()
        if self.direction == 'n':
            ret += str(self.world.getPoint(self.x - 2, self.y - 2)) #1
            self.scanScore(self.x - 2 , self.y - 2)
            ret += str(self.world.getPoint(self.x - 1, self.y - 2)) #2
            self.scanScore(self.x - 1 , self.y - 2)
            ret += str(self.world.getPoint(self.x - 0, self.y - 2)) #3
            self.scanScore(self.x - 0 , self.y - 2)
            ret += str(self.world.getPoint(self.x + 1, self.y - 2)) #4
            self.scanScore(self.x + 1 , self.y - 2)
            ret += str(self.world.getPoint(self.x + 2, self.y - 2)) #5
            self.scanScore(self.x + 2 , self.y - 2)
            ret += str(self.world.getPoint(self.x - 1, self.y - 1)) #6
            self.scanScore(self.x - 1 , self.y - 1)
            ret += str(self.world.getPoint(self.x - 0, self.y - 1)) #7
            self.scanScore(self.x - 0 , self.y - 1)
            ret += str(self.world.getPoint(self.x + 1, self.y - 1)) #8
            self.scanScore(self.x + 1 , self.y - 1)
        elif self.direction == 's':
            ret += str(self.world.getPoint(self.x + 2, self.y + 2)) #1
            self.scanScore(self.x + 2 , self.y + 2)
            ret += str(self.world.getPoint(self.x + 1, self.y + 2)) #2
            self.scanScore(self.x + 1 , self.y + 2)
            ret += str(self.world.getPoint(self.x + 0, self.y + 2)) #3
            self.scanScore(self.x + 0 , self.y + 2)
            ret += str(self.world.getPoint(self.x - 1, self.y + 2)) #4
            self.scanScore(self.x - 1 , self.y + 2)
            ret += str(self.world.getPoint(self.x - 2, self.y + 2)) #5
            self.scanScore(self.x - 2 , self.y + 2)
            ret += str(self.world.getPoint(self.x + 1, self.y + 1)) #6
            self.scanScore(self.x + 1 , self.y + 2)
            ret += str(self.world.getPoint(self.x + 0, self.y + 1)) #7
            self.scanScore(self.x + 0 , self.y + 2)
            ret += str(self.world.getPoint(self.x - 1, self.y + 1)) #8
            self.scanScore(self.x - 1 , self.y + 2)
        elif self.direction == 'e':
            ret += str(self.world.getPoint(self.x + 2, self.y - 2)) #1
            self.scanScore(self.x + 2 , self.y - 2)
            ret += str(self.world.getPoint(self.x + 2, self.y - 1)) #2
            self.scanScore(self.x + 2 , self.y - 1)
            ret += str(self.world.getPoint(self.x + 2, self.y - 0)) #3
            self.scanScore(self.x + 2 , self.y - 0)
            ret += str(self.world.getPoint(self.x + 2, self.y + 1)) #4
            self.scanScore(self.x + 2 , self.y + 1)
            ret += str(self.world.getPoint(self.x + 2, self.y + 2)) #5
            self.scanScore(self.x + 2 , self.y + 2)
            ret += str(self.world.getPoint(self.x + 1, self.y - 1)) #6
            self.scanScore(self.x + 1 , self.y - 1)
            ret += str(self.world.getPoint(self.x + 1, self.y + 0)) #7
            self.scanScore(self.x + 1 , self.y + 0)
            ret += str(self.world.getPoint(self.x + 1, self.y + 1)) #8
            self.scanScore(self.x + 1 , self.y + 1)
        elif self.direction == 'w':
            ret += str(self.world.getPoint(self.x - 2, self.y + 2)) #1
            self.scanScore(self.x - 2 , self.y + 2)
            ret += str(self.world.getPoint(self.x - 2, self.y + 1)) #2
            self.scanScore(self.x - 2 , self.y + 1)
            ret += str(self.world.getPoint(self.x - 2, self.y + 0)) #3
            self.scanScore(self.x - 2 , self.y + 0)
            ret += str(self.world.getPoint(self.x - 2, self.y - 1)) #4
            self.scanScore(self.x - 2 , self.y - 1)
            ret += str(self.world.getPoint(self.x - 2, self.y - 2)) #5
            self.scanScore(self.x - 2 , self.y - 2)
            ret += str(self.world.getPoint(self.x - 1, self.y + 1)) #6
            self.scanScore(self.x - 1 , self.y + 1)
            ret += str(self.world.getPoint(self.x - 1, self.y + 0)) #7
            self.scanScore(self.x - 1 , self.y + 0)
            ret += str(self.world.getPoint(self.x - 1, self.y - 1)) #8
            self.scanScore(self.x - 1 , self.y - 1)

        self.world.worldLock.release()
        self.rovLock.release()
        self.log.write('s', ret, self.score)
        return ret

    def scanScore(self, x, y):
        if not self.mapStat[x][y][0]:
            self.mapStat[x][y][0] = True
            hit = str(self.world.getPoint(x,y)) 
            if hit == '.' or hit == 'R':
                self.score += 1
            elif hit == 'O':
                self.score += 2
            elif hit == 'S':
                self.score += 15
            elif hit == 'W':
                self.score += 10
            elif hit == 'K':
                self.score += 100
            elif hit == 'X':
                self.score += 25
            elif hit == 'M':
                self.score += 101
                self.log.write('s', "You found a Marsian. It is incredible, it is unbelievable. Marsians do not exist you know", self.score)
            else:
                self.score += 50 


    def rotate(self, d):
        self.rovLock.acquire()
        if d == 'r':
            if self.direction == 'n':
                self.direction = 'e'
            elif self.direction == 'e':
                self.direction = 's'
            elif self.direction == 's':
                self.direction = 'w'
            elif self.direction == 'w':
                self.direction = 'n'
            self.log.write('r', self.direction, self.score)
        elif d == 'l':
            if self.direction == 'n':
                self.direction = 'w'
            elif self.direction == 'w':
                self.direction = 's'
            elif self.direction == 's':
                self.direction = 'e'
            elif self.direction == 'e':
                self.direction = 'n'
            self.log.write('l', self.direction, self.score)
        time.sleep(0.5)
        self.rovLock.release()

    def pushingRover(self, victim, rx, ry, vx, vy):
        behind = str(self.world.getPoint(vx, vy))
        if behind in self.world.notwalkable or behind == 'R':
            #print("not pushing")
            return
        #print("pushing")
        self.world.putOnWorldMap(self.x, self.y, self.under)
        self.world.putOnWorldMap(victim.x, victim.y, victim.under)
        point = self.world.getPoint(rx, ry)
        victim.under = self.world.getPoint(vx, vy)
        self.under = point
        victim.x = vx
        victim.y = vy
        self.x = rx
        self.y = ry
        self.world.putOnWorldMap(self.x, self.y, self)
        self.world.putOnWorldMap(victim.x, victim.y, victim)
        self.pushScore(victim)


    def moveForeward(self):
        self.rovLock.acquire()
        time.sleep(0.5)
        self.world.worldLock.acquire()
        if self.direction == 'n':
            point = str(self.world.getPoint(self.x, self.y - 1))
            if point in self.world.notwalkable:
                dum = 0
            elif point == ".":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.y = self.y - 1
                self.world.putOnWorldMap(self.x, self.y, self)
            elif point == "R": #push another rover
                rx = self.x
                ry = self.y - 1
                victim = self.world.getPoint(rx, ry)
                self.pushScore(victim)
                point = str(self.world.getPoint(self.x, self.y - 2))
                if point in self.world.notwalkable:
                    dum = 0
                victim = self.world.getPoint(rx, ry)
                vx = victim.x
                vy = victim.y - 1
                self.pushingRover(victim, rx, ry, vx, vy)
            elif point == "X":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.y = self.y - 1
                self.world.putOnWorldMap(self.x, self.y, self)
                self.getDataPacet(self.x, self.y)
        elif self.direction == 's':
            point = str(self.world.getPoint(self.x, self.y + 1))
            if point in self.world.notwalkable:
                dum = 0
            elif point == ".":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.y = self.y + 1
                self.world.putOnWorldMap(self.x, self.y, self)
            elif point == "R": #push another rover
                rx = self.x
                ry = self.y + 1
                victim = self.world.getPoint(rx, ry)
                self.pushScore(victim)
                point = str(self.world.getPoint(self.x, self.y + 2))
                if point in self.world.notwalkable:
                    dum = 0
                victim = self.world.getPoint(rx, ry)
                vx = victim.x
                vy = victim.y + 1
                self.pushingRover(victim, rx, ry, vx, vy)
            elif point == "X":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.y = self.y + 1
                self.world.putOnWorldMap(self.x, self.y, self)
                self.getDataPacet(self.x, self.y)
        elif self.direction == 'w':
            point = str(self.world.getPoint(self.x - 1, self.y))
            if point in self.world.notwalkable:
                dum = 0
            elif point == ".":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.x = self.x - 1
                self.world.putOnWorldMap(self.x, self.y, self)
            elif point == "R": #push another rover
                rx = self.x - 1
                ry = self.y
                victim = self.world.getPoint(rx, ry)
                self.pushScore(victim)
                point = str(self.world.getPoint(self.x - 2, self.y))
                if point in self.world.notwalkable:
                    dum = 0
                victim = self.world.getPoint(rx, ry)
                vx = victim.x - 1
                vy = victim.y
                self.pushingRover(victim, rx, ry, vx, vy)
            elif point == "X":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.x = self.x - 1
                self.world.putOnWorldMap(self.x, self.y, self)
                self.getDataPacet(self.x, self.y)
        elif self.direction == 'e':
            point = str(self.world.getPoint(self.x + 1, self.y))
            if point in self.world.notwalkable:
                dum = 0
            elif point == ".":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.x = self.x + 1
                self.world.putOnWorldMap(self.x, self.y, self)
            elif point == "R": #push another rover
                rx = self.x + 1
                ry = self.y
                victim = self.world.getPoint(rx, ry)
                self.pushScore(victim)
                point = str(self.world.getPoint(self.x + 2, self.y))
                if point in self.world.notwalkable:
                    dum = 0
                vx = victim.x + 1
                vy = victim.y
                self.pushingRover(victim, rx, ry, vx, vy)
            elif point == "X":
                self.world.putOnWorldMap(self.x, self.y, self.under)
                self.under = point
                self.x = self.x + 1
                self.world.putOnWorldMap(self.x, self.y, self)
                self.getDataPacet(self.x, self.y)
        self.world.worldLock.release()
        self.rovLock.release()
    
    def pushScore(self, vic):
        if self.lastPush != vic.rid:
            self.score += 99
            self.lastPush = vic.rid
        msg = 'You pushed ROVER ' + str(vic.color)
        self.log.write('m', msg, self.score)
        vic.log.pushed(self.color)

    def getDataPacet(self, x, y):
        if x == 101 and y == 6:
            if not self.data[0]:
                self.data[0] = True
                self.score += 50
                self.log.write('dataPackage', "Captain's log 995: It is getting close. I don't know if I can survive any longer. The food is out. The water is undrinkable. I might as well end it.", self.score)
        elif x == 92 and y == 2:
            if not self.data[1]:
                self.data[1] = True
                self.score += 50
                self.log.write('dataPackage', "Captain's log 405: I can't believe it ... suddenly it just stands there!!!", self.score)


    def drill(self):
        self.rovLock.acquire()
        x = 0
        y = 0
        if self.direction == 'n':
            x = self.x
            y = self.y  - 1
        elif self.direction == 's':
            x = self.x
            y = self.y + 1
        elif self.direction == 'e':
            x = self.x + 1
            y = self.y
        elif self.direction == 'w':
            x = self.x - 1 
            y = self.y
                
        rand = random.randint(0,99)
        result = ""
        target = str(self.world.getPoint(x, y))
        if (self.mapStat[x][y][1] == False):
            self.mapStat[x][y][1] = True
            self.score += 5
            if target == 'O': 
                if rand < 5:
                    result = "Irridium found!"
                    self.score += 100
            elif target == 'W':
                if rand < 20:
                    result = "Water found!"
                    self.score += 25
            elif target == 'R':
                vic = self.world.getPoint(x, y)
                vic.log.drilled(self.color)

                result = "You drilled ROVER " + str(vic.color) + ", you mad genius!!!"
                if self.lastDrill != vic.rid:
                    self.score += 50
                    self.lastDrill = vic.rid

        self.log.write('d', result, self.score) 
        time.sleep(0.5)
        self.rovLock.release()

    def getLog(self):
        return self.log.get()
