import numpy as np


def erreur_pour_plusieurs_parametres(
    coefficient_matrix, intercept_matrix, df, predictor_col, target_col
):
    combinaisons = np.array(
        [coefficient_matrix.reshape(-1), intercept_matrix.reshape(-1)]
    )
    erreurs = []
    shape_coefficient_matrix = coefficient_matrix.shape
    size_coefficient_matrix = shape_coefficient_matrix[0] * shape_coefficient_matrix[1]
    for index_col in range(0, size_coefficient_matrix):
        combinaison = combinaisons[:, index_col]
        erreur = calculer_erreur(combinaison, df, predictor_col, target_col)
        erreurs.append(erreur)
    return np.reshape(erreurs, shape_coefficient_matrix)


def calculer_erreur(beta, df, predictor_col, target_col):
    coefficient, intercept = beta
    prediction = coefficient * df[predictor_col] + intercept
    erreur_quadratique = (df[target_col] - prediction) ** 2
    return np.sqrt(np.mean(erreur_quadratique))
