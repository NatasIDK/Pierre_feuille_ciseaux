import random
a = ["pierre", "feuille", "ciseaux"]
scoreU = 0
scoreO = 0
reponse = input("connais-tu les regle du jeu ? oui/non : " )
if reponse == "oui":
    print("Heuresement")
else:
    print("vas sur ca ca t'aidera : https://www.regles-jeux-plein-air.com/regle-du-pierre-feuille-ciseaux")


#ChoixU = str(input("choisis entre pierre, feuille, ciseaux : " ))


while True:
    ChoixO = random.choice(a)
    ChoixU = str(input("choisis entre pierre, feuille, ciseaux : "))
    if scoreU == 3 or scoreO == 3:
        break
    elif ChoixU == ChoixO:
        print("égalité score = ", scoreU,"/", scoreO)
    elif ChoixU == "pierre" and ChoixO == "feuille":
        scoreO = scoreO + 1
        print ("ta perdu score = ", scoreU,"/", scoreO)
    elif ChoixU == "pierre" and ChoixO == "ciseaux":
        scoreU = scoreU + 1
        print("ta gagné = ", scoreU,"/", scoreO)
    elif ChoixU == "feuille" and ChoixO == "pierre":
        scoreU = scoreU + 1
        print("ta gagné = ", scoreU,"/", scoreO)
    elif ChoixU == "feuille" and ChoixO == "ciseaux":
        scoreO = scoreO + 1
        print("ta perdu score = ", scoreU,"/", scoreO)
    elif ChoixU == "ciseaux" and ChoixO == "pierre":
        scoreO = scoreO + 1
        print("ta perdu score = ", scoreU, "/", scoreO)
    elif ChoixU == "ciseaux" and ChoixO == "feuille":
        scoreU = scoreU + 1
        print("ta gagné = ", scoreU, "/", scoreO)

