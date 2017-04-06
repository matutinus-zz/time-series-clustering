import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, euclidean

def cort_metric(ts1, ts2, k):
    '''
    INPUT: numpy 1D array, numpy 1D array, integer
    OUTPUT: float
    Note: low values of k will weight the distance metric more
    '''
    if len(ts1) != len(ts2):
        print "lengths of two series are different!"
        return None
    cort_num = np.sum([(ts1[t+1] - ts1[t])*(ts2[t+1] - ts2[t]) for t in range(len(ts1)-1)])
    cort_denom1 = np.sqrt(np.sum(np.square([ts1[t+1] - ts1[t] for t in range(len(ts1)-1)])))
    cort_denom2 = np.sqrt(np.sum(np.square([ts2[t+1] - ts2[t] for t in range(len(ts2)-1)])))

    cort_coef = cort_num/(cort_denom1 * cort_denom2)
    phi = 2/(1 + np.exp(k * cort_coef))
    dist = euclidean(ts1, ts2)
    d_cort = phi * dist
    return d_cort
