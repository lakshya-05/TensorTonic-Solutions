def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    min_val = min(values)
    max_val = max(values)
    if min_val == max_val:
        return [0] * len(values)
        
    w = (max(values) - min(values))/num_bins
    res = list()
    for i in values:
        x = min(int((i-min(values))/w), num_bins-1)
        res.append(x)
    # print(res)
    return res