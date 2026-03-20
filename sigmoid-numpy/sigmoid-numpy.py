import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    X = np.asarray(x, dtype=float)
    denominator = 1 + np.exp(-X)
    sol = 1/denominator
    return sol
    