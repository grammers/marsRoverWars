# mars worl class create a world
from threading import Lock
import fileio

class Mars:
    SIZEX = 102
    SIZEY = 102

    worldMap = []

    def __init__(self, mapadr):
        self.notwalkable = ["O", "S", "W", "K", "M", "|", "_", "/", "\\"]
        self.worldMap = fileio.readinMap(mapadr)
        self.worldLock = Lock()

    def printworldmap(self):
        for x in self.worldMap:
            for y in x:
                print(str(y), end='')
            print('|')

    def getPoint(self, x, y):
        return self.worldMap[y][x]


    def putOnWorldMap(self, x, y, c):
        self.worldMap[y][x] = c
