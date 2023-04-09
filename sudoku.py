#!usr/bin/python3

# Librairie

import random
import sys

# ###############################

grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]


# ###############################
# Constante

NB_CASE_VIDE = 50  # Approximation du nombre de case vide.

# ###############################
# Fonctions

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""


def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1, 9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1],
              ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def unique(x):
    """Vérifie si tous les éléments d'une liste x sont différents."""
    liste = []   # liste de vérification.
    for i in range(len(x)):
        if x[i] == 0:   # Si une case est égale à 0, ne fait rien.
            pass
        elif x[i] in liste:
            # Si élément déjà dans la liste de vérification "liste" alors faux
            # car élément en double.
            return False
        else:   # Si élément pas encore de la liste de vérification "liste", alors l'y ajoute.
            liste.append(x[i])
    return True


def ligne(x, i):
    """
    Renvoie la ligne i de la grille de sudoku x
    """
    return x[i-1]


def colonne(x, i):
    """Renvoie la colonne i de la grille de sudoku x."""
    liste = []

    for k in range(9):  # parcours toutes les listes de la grille x.
        liste.append(x[k][i-1])

    return liste


def region(x, k):
    """Renvoie la liste de la région k de la grille de sudoku x."""
    liste = []

    for i in range(1, 10):   # parcours toutes les lignes de la grille x.
        for j in range(1, 10):  # parcours toutes les colonnes de la grille x.
            if (3*((i-1)//3) + ((j-1)//3) + 1) == k:
                # si la case (i, j) se trouve dans la région k.
                liste.append(x[i-1][j-1])   # alors ajoute la case à la liste.

    return liste


def ajouter(x, i, j, v):
    """Ajoute un élément v à la grille x de Sudoku que si celle-ci respecte
    les règles du jeu. """
    stock_v = x[i-1][j-1]  # stocke la valeur à la case i, j.
    x[i-1][j-1] = v  # ajoute la valeur v à l'emplacement i, j.
    k = (3*((i-1)//3) + ((j-1)//3) + 1)   # calcul la valeur de la région.

    # Vérification de l'ajout de la valeur v par rapport aux règles du sudoku.
    # Si conflit de valeur sur une ligne ou une colonne ou une région
    # Ou si présente de case vide (0)
    # Alors remet la case modifiée vide (0).
    if (not unique(ligne(x, i))) or (not unique(colonne(x, j))) or\
       (not unique(region(x, k))):
        x[i-1][j-1] = stock_v


def verifier(x):
    "Vérifie si la grille x de Sudoku est correctement remplie."

    for m in range(len(x)):  # parcours toutes les lignes, colonnes et régions.
        if not unique(ligne(x, m)) or not unique(colonne(x, m)) or\
           not unique(region(x, m)) or (0 in x[m]):
            # si 2 (ou plus) fois la meme valeur dans une ligne, région our
            # colonne.
            return False

    return True


def jouer(x):
    """Permet à l'utilisateur de pouvoir rentrer une nouvelle valeur
    dans la grille x, aux coordonnées souhaitées.

    Affiche la nouvelle grille de Sudoku avec la nouvelle valeur
    (ou non, si pas compatible avec les règles du jeu)"""

    nb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for n in range(len(x)):
        if 0 in x[n]:  # si grille pas encore remplie.
            reponse = (input("Entrer votre réponse sous la forme: ligne, colonne, valeur:"))
            liste = []
            liste2 = []
            for car in reponse:
                liste.append(car)  # transformation du tuple "reponse" entré
                # par l'utilisateur sous forme de liste.

            # Supprime les éléments indésirables de liste.
            # C'est-à-dire, les virgules, espaces et parenthèses.
            # Car liste est de la forme:
            # ['(', 'i', ',', ' ', 'j', ',', ' ', 'v', ')']
            for m in range(len(liste)):
                if liste[m] in nb:  # si l'élément de la liste est bien un nb.
                    liste2.append(liste[m])  # on l'ajoute à liste2.

            ajouter(x, int(liste2[0]), int(liste2[1]), int(liste2[2]))
            afficher(x)
            jouer(x)


def solutions(x):
    """Renvoie les valeurs potentielles de chaque case vide sous forme d'un
    dictionnaire: dico de la grille:x."""

    nb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    l9 = []
    dico = {0: l0, 1: l1, 2: l2, 3: l3, 4: l4, 5: l5, 6: l6, 7: l7, 8: l8,
            9: l9}

    for i in range(1, 10):  # parcours toutes les lignes de la grille x
        for j in range(1, 10):  # parcours toutes les colonnes de x.
            if x[i-1][j-1] == 0:  # Si case vide.
                l_ligne = ligne(x, i)
                l_colonne = colonne(x, j)
                l_region = region(x, (3*((i-1)//3) + ((j-1)//3) + 1))
                l = []
                for m in range(1, 10):  # parcours les valeurs du jeu du sudoku
                    if (nb[m] not in l_ligne) and (nb[m] not in l_colonne) and\
                         (nb[m] not in l_region):
                        # si la valeur m n'est pas encore dans la ligne,
                        # colonne et région, alors on l'ajoute à la liste "l"
                        # car il s'agit de la valeur potentielle que pourra
                        # prendre la case (i, j).
                        l.append(nb[m])
                if len(l) == 1:
                    l1.append((i, j, l))
                elif len(l) == 2:
                    l2.append((i, j, l))
                elif len(l) == 3:
                    l3.append((i, j, l))
                elif len(l) == 4:
                    l4.append((i, j, l))
                elif len(l) == 5:
                    l5.append((i, j, l))
                elif len(l) == 6:
                    l6.append((i, j, l))
                elif len(l) == 7:
                    l7.append((i, j, l))
                elif len(l) == 8:
                    l8.append((i, j, l))
                elif len(l) == 9:
                    l9.append((i, j, l))
                else:
                    l0.append((i, j, l))

    return dico


def resoudre(x):
    """Permet de résoudre une grille de sudoku x."""
    dico = solutions(x)
    l = list(dico.values())

    if l[0] != []:  # Si un élement n'a pas de solution.
        return False
    if (l[0] == [] and l[1] == [] and l[2] == [] and l[3] == [] and l[4] == []
       and l[5] == [] and l[6] == [] and l[7] == [] and l[8] == [] and
       l[9] == []):  # si grille x déjà résolue.
        return x

    for m in range(len(l)):
        if l[m] != []:
            for n in range(len(l[m])):
                tuplee = l[m][n]
                i, j, v = tuplee[0], tuplee[1], tuplee[2]
                # v la liste des valeurs potentielles à mettre à la case(i, j)

                for indice in range(len(v)):
                    x[i-1][j-1] = v[indice]
                    # on met une valeur v dans la case(i,j) de la grille x.
                    resoudre(x)
                    # rappel de la fonction avec la nouvelle valeur testée.
                    if unique(ligne(x, i)) and unique(colonne(x, j)) and\
                       unique(region(x, (3*((i-1)//3) + ((j-1)//3) + 1))):
                        # si pas de conflit des valeurs dans la grille x:
                        return x
                    else:  # si conflit de valeurs: annuler l'ajout de valeur.
                        x[i-1][j-1] = 0

                return False


def generer():
    """Génère dans certain cas une grille de sudoku complète.
    Si grille générée: la grille est retournée.
    Sinon: False

    ⚠️ ATTENTION: Ne génère pas une nouvelle grille différente si on réexécute
    le programme. Il faut cliquer sur l'icone "poubelle" (tuer le programme) de
    VSCODE pour obtenir une nouvelle grille de sudoku.⚠️"""

    x = [
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 0, 0, 0, 0, 0, 0, 0, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 8],
     [0, 0, 0, 0, 0, 0, 0, 0, 6],
     [0, 0, 0, 0, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 0, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 0, 0, 0, 3],
     [0, 0, 0, 0, 0, 0, 0, 0, 2],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     ]

    random.shuffle(x)

    # ######
    # A partir d'ici on aurait pu juste écrire "return resoudre(x)" mais ce
    # n'est pas ce qui était demandé dans l'énoncé du projet.
    # ######

    dico = solutions(x)
    l = list(dico.values())

    if l[0] != []:  # Si un élement n'a pas de solution.
        return False
    if (l[0] == [] and l[1] == [] and l[2] == [] and l[3] == [] and l[4] == []
       and l[5] == [] and l[6] == [] and l[7] == [] and l[8] == [] and
       l[9] == []):  # si grille x déjà résolue.
        return x

    for m in range(len(l)):
        if l[m] != []:
            for n in range(len(l[m])):
                tuplee = l[m][n]
                i, j, v = tuplee[0], tuplee[1], tuplee[2]
                # v la liste des valeurs potentielles à mettre à la case(i, j)

                for indice in range(len(v)):
                    x[i-1][j-1] = v[indice]
                    # on met une valeur v dans la case(i,j) de la grille x.
                    resoudre(x)
                    if verifier(x):
                        # si pas de conflit des valeurs dans la grille x:
                        return x
                    else:  # si conflit de valeur: annuler l'ajout de valeur.
                        x[i-1][j-1] = 0

                return False


def nouvelle():
    """Génère une grille de sudoku à trou et la retourne."""
    global NB_CASE_VIDE

    x = generer()
    # tant que la grille générée n'est pas valide. On en génère une autre
    # jusqu'à en avoir une valide.
    while x == False:
        x = generer()

    for c in range(NB_CASE_VIDE):  # On vide environ NB_CASE_VIDE cases.
        i = random.randint(0, 8)  # choisit une ligne aléatoirement
        j = random.randint(0, 8)   # choisit une colonne aléatoirement
        x[i][j] = 0

    return x



if __name__ == "__main__":
    if sys.argv[1] == "-generer":
        ma_grille = nouvelle()  # Génère une grille de sudoku
        afficher(ma_grille)  # affiche la liste de sudoku
    
    elif sys.argv[1] == "-joue":
        ma_grille = nouvelle()
        afficher(ma_grille)
        jouer(ma_grille)

    elif sys.argv[1] == "-resoudre":
        ma_grille = nouvelle()  # Génère une grille de sudoku
        afficher(ma_grille)  # affiche la liste de sudoku
        afficher(resoudre(ma_grille))  # résoud la grille de sudoku
