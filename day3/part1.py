import string

def getListFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()
    return content

def splitStringOn2(string: str):
    string1 = ""
    string2 = ""

    for i in range(0, len(string)):
        if (i < len(string) / 2):
            string1 += string[i]
        else:
            string2 += string[i]

    return [string1, string2]

def searchItemInBothList(list: list[str]):
    for i in range(0, len(list[0])):
        indexOfItem = list[1].find(list[0][i])
        if indexOfItem != -1:
            break
    return {
        "letter": list[1][indexOfItem],
        "priority": getPriorityOfItem(list[1][indexOfItem])
    }

def getAlphabet():
    return list(string.ascii_letters)

def getPriorityOfItem(item: str):
    return getAlphabet().index(item) + 1

content = getListFromFile()

# Pour chaque ligne du fichier on coupe en 2 la ligne
contentSplited = [splitStringOn2(content[x]) for x in range(0, len(content))]

totalPriority = 0
# Pour chaque ligne on cherche l'item commun
for i in range(0, len(contentSplited)):
    item = searchItemInBothList(contentSplited[i])
    totalPriority += item["priority"]

print("Le total des prioritées de chaque type d'item est : ", totalPriority)