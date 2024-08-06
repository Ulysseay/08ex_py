
def lire_matrice(fichier_matrice):
    """Reads a matrix from a text file."""
    try:
        with open(fichier_matrice, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]
        return matrix
    except FileNotFoundError:
        print(f"Error: File {fichier_matrice} not found.")
        return None
    except ValueError:
        print(f"Error: File {fichier_matrice} contains invalid data.")
        return None

def additionner_matrices(matrice1, matrice2):
    """Adds two matrices of the same dimensions."""
    if len(matrice1) != len(matrice2) or any(len(row1) != len(row2) for row1, row2 in zip(matrice1, matrice2)):
        print("Error: Matrices must have the same dimensions.")
        return None
    return [[matrice1[i][j] + matrice2[i][j] for j in range(len(matrice1[0]))] for i in range(len(matrice1))]

def afficher_matrice(matrice):
    """Displays a matrix."""
    if matrice:
        for row in matrice:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Read the matrices from the files
    matrice1 = lire_matrice('matrice1.txt')
    matrice2 = lire_matrice('matrice2.txt')

    if matrice1 and matrice2:
        # Add the matrices
        result = additionner_matrices(matrice1, matrice2)

        # Display the result
        if result:
            print("Result of the matrix addition:")
            afficher_matrice(result)


