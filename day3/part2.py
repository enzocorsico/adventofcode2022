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

def searchCommunItemOf3Lines(list: list[str]):
    for i in range(0, len(list[0])):
        indexOfItemInList2 = list[1].find(list[0][i])
        indexOfItemInList3 = list[2].find(list[0][i])
        if indexOfItemInList2 != -1 and indexOfItemInList3 != -1:
            break

    communLetter = list[1][indexOfItemInList2]
    return {
        "letter": communLetter,
        "priority": getPriorityOfItem(communLetter)
    }

def getAlphabet():
    return list(string.ascii_letters)

def getPriorityOfItem(item: str):
    return getAlphabet().index(item) + 1

content = getListFromFile()

# On regroupe les lignes par 3
contentPer3 = [content[x:x+3] for x in range(0, len(content), 3)]

totalPriority = 0
# Pour chaque ligne on cherche l'item commun
for i in range(0, len(contentPer3)):
    item = searchCommunItemOf3Lines(contentPer3[i])
    totalPriority += item["priority"]

print("Le total des prioritées de chaque type d'item est : ", totalPriority)