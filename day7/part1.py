def getContentFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()
    return content

content = getContentFromFile()

for i in range(len(content)):
    line = content[i].split(" ")
    print(line)
