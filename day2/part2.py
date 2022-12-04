def getListFromFile():
    file = open("puzzle.txt", "r")
    content = file.read().splitlines()
    file.close()

    # Pour chaque ligne, on split pour passer de ["A B"] à ["A", "B"]
    content = [line.split(" ") for line in content]
    return content

def getShapePoints():
    return {
        "A": {
            "strength": "C",
            "weakness": "B",
            "points": 1
        },
        "B": {
            "strength": "A",
            "weakness": "C",
            "points": 2
        },
        "C": {
            "strength": "B",
            "weakness": "A",
            "points": 3
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

    if match[1] == "X": # Si le match doit être une défaite
        strengthLetter = shapesPoints[match[0]]["strength"]
        return {
            "status": "Lose",
            "points": shapesPoints[strengthLetter]["points"] + 0
        }
    elif match[1] == "Y": # Si le match doit être une égalité
        return {
            "status": "Draw",
            "points": shapesPoints[match[0]]["points"] + 3
        }
    else: # Si le match doit être une victoire
        weaknessLetter = shapesPoints[match[0]]["weakness"]
        return {
            "status": "Win",
            "points": shapesPoints[weaknessLetter]["points"] + 6
        }

puzzle = getListFromFile()

score = calculScore(puzzle)

print("Nombre de victoires : ", score["numberOfWin"])
print("Nombre de matchs nuls : ", score["numberOfDraw"])
print("Nombre de défaites : ", score["numberOfLose"])
print("Nombre de points : ", score["totalPoints"])