def addScore(name, score):
    data = getScoreSorted()
    print(data)
    file = open("View/Data/score.txt", "w")
    i = 0
    file.write(',')
    while i < len(data):
        file.write("%s,%s," % (data[i], data[i + 1]))
        i += 2

    file.write("%s,%s" % (name, score))


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
    if data != '':
        while i < len(data):
            tabTuple.append((data[i], data[i+1]))
            i += 2
        tabTuple.sort(key=lambda tup: tup[1], reverse=True)  # sorts
        return tabTuple