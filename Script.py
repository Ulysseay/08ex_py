

import numpy as np

def add_matrices(matrix1, matrix2):
    try:
        # Convertion des listes en matrices numpy
        mat1 = np.array(matrix1)
        mat2 = np.array(matrix2)
        
        # Vérificationde la compatibilité  pour l'addition
        if mat1.shape != mat2.shape:
            raise ValueError("Les matrices doivent avoir les mêmes dimensions pour être additionnées")
        
        # Additionn des matrices
        result = mat1 + mat2
        return result
    except Exception as e:
        return str(e)

import tkinter as tk
from tkinter import messagebox
import numpy as np

def add_matrices_gui():
    def on_add():
        try:
            matrix1 = eval(entry_matrix1.get())
            matrix2 = eval(entry_matrix2.get())
            result = add_matrices(matrix1, matrix2)
            result_label.config(text=f"Résultat: {result}")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
    
    def add_matrices(matrix1, matrix2):
        try:
            mat1 = np.array(matrix1)
            mat2 = np.array(matrix2)
            if mat1.shape != mat2.shape:
                raise ValueError("Les matrices doivent avoir les mêmes dimensions pour être additionnées")
            result = mat1 + mat2
            return result
        except Exception as e:
            return str(e)

    root = tk.Tk()
    root.title("Additionneur de Matrices")
    
    tk.Label(root, text="Matrice 1 (ex: [[1, 2], [3, 4]]):").pack()
    entry_matrix1 = tk.Entry(root, width=50)
    entry_matrix1.pack()

    tk.Label(root, text="Matrice 2 (ex: [[5, 6], [7, 8]]):").pack()
    entry_matrix2 = tk.Entry(root, width=50)
    entry_matrix2.pack()

    add_button = tk.Button(root, text="Additionner", command=on_add)
    add_button.pack()

    result_label = tk.Label(root, text="Résultat: ")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    add_matrices_gui()



