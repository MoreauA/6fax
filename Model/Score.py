def addScore(dst, name, score):
    dst.write("%s,%s\n" % (name, score))


def getScore():
    file = open("View/Data/score.txt")
    data = file.read()
    data = data.split(",")
    for i in range(len(data)):
        if i%2 == 1:
            data[i] = int(data[i])
    file.close()
    return data

def getScoreSorted():
    data = getScore()
    tabTuple = []
    i = 0
    while i < len(data):
        tabTuple.append((data[i], data[i+1]))
        i += 2
    tabTuple.sort(key=lambda tup: tup[1], reverse=True)  # sorts
    return tabTuple
