def getStringFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()
    return content[0]

def getMarkerIndex(string: str, markerSize: int):
    for i in range(len(string)):
        if (len(string[i:i+markerSize]) == markerSize):
            temp = [*string[i:i+markerSize]]
            if not checkDoublon(temp):
                return i + markerSize

def checkDoublon(array: list[str]):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if (array[i] == array[j]):
                return True
    return False
    

string = getStringFromFile()

markerIndex = getMarkerIndex(string, 4)

print("L'index du premier marker est : " + str(markerIndex))