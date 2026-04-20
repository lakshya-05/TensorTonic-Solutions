import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    res = np.maximum(0, x)
    return res