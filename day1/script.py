import requests

def getListFromFile():
    file = open("list.txt", "r")
    content = file.read().splitlines()
    file.close()
    return content

def calculateTotalCaloriesByElf(list: list):
    totalCaloriesByElf = []
    currentCalories = 0
    for calories in content:
        if calories != "":
            currentCalories += int(calories)
        else:
            totalCaloriesByElf.append(currentCalories)
            currentCalories = 0
    return totalCaloriesByElf

def getMostCaloriesAndIndex(totalCaloriesByElf: list):
    mostCalories = 0
    mostCaloriesIndex = 0
    for index, calories in enumerate(totalCaloriesByElf):
        if calories > mostCalories:
            mostCalories = calories
            mostCaloriesIndex = index
    return mostCalories, mostCaloriesIndex

# On récupère la liste des calories depuis le site
content = getListFromFile()

# On calcule le nombre total de calories par elfe
totalCaloriesByElf = calculateTotalCaloriesByElf(content)

# On récupère l'elfe qui a récupéré le plus de calories puis on le supprime de la liste
firstElf = getMostCaloriesAndIndex(totalCaloriesByElf)
totalCaloriesByElf.pop(firstElf[1])

# On récupère le deuxième l'elfe qui a récupéré le plus de calories puis on le supprime de la liste
secondElf = getMostCaloriesAndIndex(totalCaloriesByElf)
totalCaloriesByElf.pop(secondElf[1])

# On récupère le troisième l'elfe qui a récupéré le plus de calories puis on le supprime de la liste
thirdElf = getMostCaloriesAndIndex(totalCaloriesByElf)
totalCaloriesByElf.pop(thirdElf[1])

# Affichage des résultats
print("Classement des calories récupéré par elfe est :")
print(" - 1er : ", firstElf[0])
print(" - 2ème : ", secondElf[0])
print(" - 3ème : ", thirdElf[0])
print("Le gagnant est l'elfe numéro : ", firstElf[1] + 1)
print("La somme des calories récupéré des 3 premiers elfes est de : ", firstElf[0] + secondElf[0] + thirdElf[0])