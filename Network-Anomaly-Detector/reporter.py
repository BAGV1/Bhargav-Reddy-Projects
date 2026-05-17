import pandas as pd

def create_report(sizes, scores):
    data_mapping = {'Sizes': sizes, 'Z-Score': scores}
    report_table = pd.DataFrame(data_mapping)
    # Taking absolute value is an easy way to
    # get both high and low anomalies
    absolute_scores = report_table['Z-Score'].abs()
    anomalies = report_table[absolute_scores > 2.5]
    return anomalies
