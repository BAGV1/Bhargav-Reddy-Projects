"""
The sole purpose of this file is to
calculate the packet Z-Score
"""
import numpy as np
from scipy.stats import zscore

def calculate_anomalies(data_list):
    data_list = np.array(data_list)
    scores = zscore(data_list)
    return scores
