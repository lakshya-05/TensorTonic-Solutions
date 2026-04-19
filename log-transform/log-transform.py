def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    res = list()
    for i in values:
        res.append(np.log(1+i))

    return res