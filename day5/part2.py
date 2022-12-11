def getContentFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()
    return content

def getNumberOfStacks(content: list[str]):
    temp: list[int] = []
    for char in content:
        if (char != " "):
            temp.append(int(char))
    return temp[-1]

def splitContent(content: list[str]):
    stocks: list[list[str]] = []
    instructions: list[dict[str, int]] = []

    temp_stocks: list[str] = []
    for i in range(content.index("")):
        temp_stocks.append(content[i])
    numberOfStacks = getNumberOfStacks(temp_stocks[-1])

    # Ajout d'une liste vide pour chaque stack
    for i in range(numberOfStacks):
        stocks.append([])

    # Mise en forme des stacks
    for i in range(content.index("") - 1):
        ligne = [*content[i]]

        temp_stacks: list[list] = []
        for x in range(0, numberOfStacks * 4, 4):
            temp_stacks.append(ligne[x:x+4][1])

        for x in range(numberOfStacks):
            if (temp_stacks[x] != " "):
                stocks[x].append(temp_stacks[x])

    # Mise en forme des instructions
    for i in range(content.index("") + 1, len(content)):
        instructions.append({
            "quantity": int(content[i].split(" ")[1]),
            "from": int(content[i].split(" ")[3]) - 1,
            "to": int(content[i].split(" ")[5]) - 1
        })

    return stocks, instructions

def moveByInstructions(stocks: list[list[str]], instructions: list[dict[str, int]]):
    for instruction in instructions:
        tempMovedItems = []
        for i in range(instruction["quantity"]):
            tempMovedItems.append(stocks[instruction["from"]].pop(0))

        for i in range(len(tempMovedItems)):
            stocks[instruction["to"]].insert(i, tempMovedItems[i])
    
    return stocks

def getMessage(stocks: list[list[str]]):
    message = ""
    for stock in stocks:
        message += stock[0]

    return message

content = getContentFromFile()

stocks, instructions = splitContent(content)

finalStocks = moveByInstructions(stocks, instructions)

message = getMessage(finalStocks)

print("Le message est : ", message)