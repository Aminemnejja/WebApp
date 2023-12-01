import numpy as np
from fractions import Fraction

def float_to_fraction_string(value):
    fraction = Fraction(value).limit_denominator()

    # Vérifier si la fraction représente un entier
    if 1 == fraction.denominator:
        return str(fraction.numerator)
    else:
        return f"{fraction.numerator}/{fraction.denominator}"

def matrix_to_fraction(matrix):
    # Obtenir la dimension de la matrice
    num_rows, num_cols = matrix.shape if matrix.ndim == 2 else (matrix.size, 1)

    # Appliquer la fonction float_to_fraction_string à chaque élément de la matrice
    fraction_matrix = [
        [float_to_fraction_string(matrix[i]) if matrix.ndim == 1 else float_to_fraction_string(matrix[i, j]) for j in range(num_cols)]
        for i in range(num_rows)
    ]

    if num_cols == 1:
        return np.array([row[0] for row in fraction_matrix])
    else:
        return np.array(fraction_matrix)

