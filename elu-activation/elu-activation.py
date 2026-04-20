import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    res = list()
    for i in x:
        if i > 0:
            res.append(i)
        else:
            res.append(alpha*(np.exp(i)-1))
    return res