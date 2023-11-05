# looger for marsrover
from datetime import datetime

class Logger:
    def __init__(self, rid, color):
        self.fileName = "loggs/" + str(rid) + ".log"
        
        ''' uncoment if a clean start is wanted
        f = open(self.fileName, "w")
        f.write("")
        f.cose()
        '''
        self.write("start", 
            "Rover " + str(color) + " has started!", 0)

    def write(self, comand, messages, score):
        return
        msg = str(datetime.now().time())
        msg += "-" + comand
        if score == 0:
            msg += "-\"" + messages +"\"\n"
        else:
            msg += "-\"" + messages + " score:" + str(score) +"\"\n"

        f = open(self.fileName, "a")
        f.write(msg)
        f.close()
    
    def pushed(self, color):
        return
        msg = str(datetime.now().time())
        msg += "-\"" + "You have been pushed by rover " + str(color) + "\"\n"

        f = open(self.fileName, "a")
        f.write(msg)
        f.close()

    def readLog(self):
        return
        log = []
        f = open(self.fileName, "r")
        for line in f:
            log.append(line)
        f.close()
        return log
        
    def drilled(self, color):
        return
        msg = str(datetime.now().time())
        msg += "-\"Rover " + str(color) + " have drilled you\""

        f = open(self.fileName, "a")
        f.write(msg)
        f.close()

    def get(self):
        return
        f = open(self.fileName, "r")
        content = f.read()
        f.close()
        return content
