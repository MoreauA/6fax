def addScore(file,name, score):
    data = getScoreSorted(file)

    print(data)
    file = open("View/Data/score" + str(file)+ ".txt", "w")
    i = 1
    file.write(str(data[0][0]) + "," + str(data[0][1]) + ",")
    while i < len(data) and i <10:
        file.write(str(data[i][0]) + "," + str(data[i][1]) + ",")
        i += 1

    file.write("%s,%s" % (name[:-1], score))


def getAllScore(file):
    file = open("View/Data/score" + str(file) + ".txt")
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
