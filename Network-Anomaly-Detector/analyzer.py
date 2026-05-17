"""
The sole purpose of this file is to
calculate the packet Z-Score
"""
import numpy as np
from scipy.stats import zscore

"""
Find Size Distribution, Time Intervals
Computes Z-Scores for both to find anomalies
"""
def calculate_anomalies(sizes, times):
    sizes = np.array(sizes)

    time_intervals = np.diff(times)
    sizes = sizes[1:]

    scores = zscore(sizes)
    time_scores = zscore(time_intervals)

    return scores, time_scores
