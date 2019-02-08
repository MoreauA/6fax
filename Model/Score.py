def addScore(file,name, score):
    data = getScoreSorted(file)

    file = open("View/Data/Scores/score" + str(file)+ ".txt", "w")
    i = 1
    file.write(str(data[0][0]) + "," + str(data[0][1]) + ",")
    while i < len(data) and i <10:
        file.write(str(data[i][0]) + "," + str(data[i][1]) + ",")
        i += 1

    file.write("%s,%s" % (name[:-1], score))


def getAllScore(file):
    file = open("View/Data/Scores/score" + str(file) + ".txt")
    data = file.read()
    data = data.split(",")
    for i in range(len(data)):
        if i%2 == 1:
            data[i] = int(data[i])
    file.close()
    return data

def getScoreSorted(file):
    data = getAllScore(file)
    tabTuple = []
    i = 0
    if data != '':
        while i < len(data):
            tabTuple.append((data[i], data[i+1]))
            i += 2
        tabTuple.sort(key=lambda tup: tup[1], reverse=True)  # sorts
        return tabTuple

def getAllMapState():
    file = open("View/Data/Unlock/mapState.txt")
    data = file.read()
    data = data.split(",")
    for i in range(len(data)):
            data[i] = int(data[i])

    file.close()
    tabTuple = []
    i = 0
    if data != '':
        while i < len(data)-1:
            tabTuple.append((data[i], data[i + 1]))
            i += 2
        tabTuple.sort(key=lambda tup: tup[0])  # sorts

    return tabTuple

def updateMapState(level,state):
    data = getAllMapState()
    file = open("View/Data/Unlock/mapState.txt", "w")
    i = 0
    while i < len(data):
        if data[i][0] != level:
            file.write(str(data[i][0]) + "," + str(data[i][1]) + ",")
        i += 1

    file.write("%s,%s" % (level,state))

def reinit(src,dest):
    filesrc = open("View/Data/" + src + ".txt", "r")
    filedest = open("View/Data/" + dest + ".txt", "w")
    data = filesrc.read()
    filedest.write(data)



