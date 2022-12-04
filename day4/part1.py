def getListFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()
    return content

def splitContent(content: list[str]):
    tempContent = []
    for pair in content:
        temp = []
        for item in pair.split(","):
            temp.append(item.split("-"))
        tempContent.append(temp)
    
    return tempContent

def calculAssignmentPairs(content: list[list[list[str]]]):
    total = 0
    for pair in content:
        for item in pair:
            # On transforme les valeurs en int
            item[0] = int(item[0])
            item[1] = int(item[1])

        if caculDifference(pair[0]) >= caculDifference(pair[1]):
            if (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
                total += 1
        else:
            if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
                total += 1
    
    return total

def caculDifference(list: list[int]):
    return list[1] - list[0]


content = getListFromFile()

contentSplited = splitContent(content)

total = calculAssignmentPairs(contentSplited)

print("Le nombre de paires est de : ", total)