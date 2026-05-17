import pandas as pd

def create_report(sizes, size_scores, time_scores):
    data_mapping = {'Sizes': sizes,
                    'Size Z-Score': size_scores,
                    'Time Z-Score': time_scores
                    }

    report_table = pd.DataFrame(data_mapping)

    # Taking absolute value is an easy way to
    # get both high and low anomalies
    size_anomalies = report_table['Size Z-Score'].abs() > 2.5
    time_anomalies = report_table['Time Z-Score'].abs() > 2.5

    anomalies = report_table[size_anomalies | time_anomalies]

    return anomalies
