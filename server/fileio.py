# file fore file io

def readinMap(maploc):
    f = open(maploc, "r")

    wmap = []
    n = 0

    buf = f.readline()
    buf = buf[:-1]
    while buf != "END":
        wmap.append([])
        for c in buf:
            wmap[n].append(c)
        n = n + 1
        buf = f.readline()
        buf = buf[:-1]

    f.close()
    return wmap
        
