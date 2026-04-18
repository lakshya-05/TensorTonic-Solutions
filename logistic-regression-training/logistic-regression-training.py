import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # print(X)
    # print(y)
    N, D = X.shape
    w, b = np.zeros(D), 0
    error = 1
    for _ in range(steps):
        pred = 1/(1+np.exp(-((X@w) + b)))
        e = pred - y
        delw = X.T @ e/N
        delb = np.mean(e)

        w = w-lr*delw
        b = b-lr*delb

    return (w,b)