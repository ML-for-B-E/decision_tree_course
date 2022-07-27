import numpy as np


def entropy_for_binary_variable(probability: float) -> float:
    return entropy([probability, 1 - probability])


def entropy(probabilities: np.array) -> float:
    if not np.isclose(sum(probabilities), 1):
        msg = f"Input {probabilities} must sum to 1"
        raise Exception(msg)

    entropy = 0
    for probability in probabilities:
        entropy += get_entropy_class(probability)
    return entropy


def get_entropy_class(probability: float) -> float:
    if np.isclose(probability, 0) or np.isclose(probability, 1):
        return 0
    return -probability * np.log2(probability)
