import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    res = list()
    for i in x:
        # print(i)
        if i >= 0:
            res.append(i)
        else:
            res.append(i*alpha)
            
    #print(res)
    return np.array(res)