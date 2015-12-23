import numpy as np 
from scipy.stats import scoreatpercentile

def ab_test(ax, an, bx, bn, percentiles=(2.5, 50, 97.5), trials=10000):
    """"""

    a_conv = np.random.beta(ax + 1, an - ax + 1, size=trials)
    b_conv = np.random.beta(bx + 1, bn - bx + 1, size=trials)

    diff = b_conv - a_conv

    diff_percentiles = [scoreatpercentile(diff, p) for p in percentiles]
    diff_percentiles.append((diff > 0).mean())
        
    return np.array(diff_percentiles)

