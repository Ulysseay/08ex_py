

def lire_matrice(fichier_matrice):
    """Lit une matrice à partir d'un fichier texte."""
    try:
        with open(fichier_matrice, 'r') as fichier:
            matrice = [list(map(int, ligne.strip().split())) for ligne in fichier]
        return matrice
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_matrice} n'a pas été trouvé.")
        return None
    except ValueError:
        print(f"Erreur : Le fichier {fichier_matrice} contient des données invalides.")
        return None
def additionner_matrices(matrice1, matrice2):
    """Additionne deux matrices de mêmes dimensions."""
    if len(matrice1) != len(matrice2) or any(len(ligne1) != len(ligne2) for ligne1, ligne2 in zip(matrice1, matrice2)):
        print("Erreur : Les matrices doivent avoir les mêmes dimensions.")
        return None
    return [[matrice1[i][j] + matrice2[i][j] for j in range(len(matrice1[0]))] for i in range(len(matrice1))]

def afficher_matrice(matrice):
    """Affiche une matrice."""
    if matrice:
        for ligne in matrice:
            print(" ".join(map(str, ligne)))

if __name__ == "__main__":
    # Lire les matrices à partir des fichiers
    matrice1 = lire_matrice('matrice1.txt')
    matrice2 = lire_matrice('matrice2.txt')

    if matrice1 and matrice2:
        # Additionner les matrices
        resultat = additionner_matrices(matrice1, matrice2)

        # Afficher le résultat
        if resultat:
            print("Résultat de l'addition des matrices :")
            afficher_matrice(resultat)    

