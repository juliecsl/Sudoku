# Sudoku

## Présentation du projet
Ce projet permet de générer des grilles de sudoku, de les résoudre et de jouer au sudoku.

## Prérequis
* Version Python: 3.8.16
* Librairies: ```random``` et ```sys```

## Utilisation
### Générer une grille de sudoku à trous
Pour générer une grille de sudoku à trous il faut éxécuter la commande suivante dans un terminal:

```python sudoku.py -generer```

### Jouer
Pour jouer au sudoku il faut exéctuer la commande suivante dans un terminal:
```python sudoku -joue```

La grille de sudoku s'affiche ainsi que le message:
> Entrer votre réponse sous la forme: ligne, colonne, valeur:

Il faut alors saisir dans le terminal la valeur que vous voulez jouer ainsi que la ligne et la colonne correspond à la case (entre 1 et 9)

* Exemple:
> Entrer votre réponse sous la forme: ligne, colonne, valeur:1,2,8

Si vous entrez une mauvaise réponse la valeur ne s'affichera pas dans la grille mais si vous entrez une bonne réponse celle-ci s'affichera. 

### Générer une grille et avoir la solution
Pour générer une grille et en connaitre la solution, il faut executer la commande suivante dans un terminal:
```python sudoku.py -resoudre```
