def getListFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()

    # Pour chaque ligne, on split pour passer de ["A B"] à ["A", "B"]
    content = [line.split(" ") for line in content]
    return content

def getShapePoints():
    return {
        "opponent": {
            "A": {
                "weakness": "Y",
                "points": 1
            },
            "B": {
                "weakness": "Z",
                "points": 2
            },
            "C": {
                "weakness": "X",
                "points": 2
            }
        },
        "me": {
            "X": {
                "weakness": "B",
                "points": 1
            },
            "Y": {
                "weakness": "C",
                "points": 2
            },
            "Z": {
                "weakness": "A",
                "points": 3
            },
        }
    }

def calculScore(puzzle: list[list[str]]):
    numberOfWin = 0
    numberOfDraw = 0
    numberOfLose = 0
    totalPoints = 0

    for line in puzzle:
        result = getMatchResult(line)
        if result["status"] == "Win":
            numberOfWin += 1
            totalPoints += result["points"]
        elif result["status"] == "Draw":
            numberOfDraw += 1
            totalPoints += result["points"]
        else:
            numberOfLose += 1
            totalPoints += result["points"]
    
    return {
        "numberOfWin": numberOfWin,
        "numberOfDraw": numberOfDraw,
        "numberOfLose": numberOfLose,
        "totalPoints": totalPoints
    }

def getMatchResult(match: list[str]):
    shapesPoints = getShapePoints()
    if shapesPoints["opponent"][match[0]]["weakness"] == match[1]:
        return {
            "status": "Win",
            "points": shapesPoints["me"][match[1]]["points"] + 6
        }
    elif shapesPoints["me"][match[1]]["weakness"] == match[0]:
        return {
            "status": "Lose",
            "points": shapesPoints["me"][match[1]]["points"] + 0
        }
    else:
        return {
            "status": "Draw",
            "points": shapesPoints["me"][match[1]]["points"] + 3
        }

puzzle = getListFromFile()

score = calculScore(puzzle)

print("Nombre de victoires : ", score["numberOfWin"])
print("Nombre de matchs nuls : ", score["numberOfDraw"])
print("Nombre de défaites : ", score["numberOfLose"])
print("Nombre de points : ", score["totalPoints"])