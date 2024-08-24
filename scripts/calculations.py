import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb # type: ignore
from scipy import stats

def summarize_statistics(df):
    # Ensure the DataFrame is numeric
    num_df = df.select_dtypes(include=['number'])
    
    # Calculate summary statistics
    summary_stats = num_df.describe().T
    
    # Additional statistics
    summary_stats['median'] = num_df.median()
    summary_stats['mode'] = num_df.mode().iloc[0]  # Mode (first mode if there are multiple)
    summary_stats['variance'] = num_df.var()
    summary_stats['range'] = num_df.max() - num_df.min()
    summary_stats['iqr'] = num_df.quantile(0.75) - num_df.quantile(0.25)
    summary_stats['skewness'] = num_df.skew()
    summary_stats['kurtosis'] = num_df.kurt()
    
    return summary_stats

def calculate_z_scores(df, columns, threshold=3):
    z_scores = pd.DataFrame()
    for col in columns:
        # Calculate Z-scores
        df[col + '_z'] = stats.zscore(df[col])
        
        # Flag outliers
        df[col + '_outlier'] = df[col + '_z'].apply(lambda x: abs(x) > threshold)
        
        # Store Z-scores in the new DataFrame
        z_scores[col] = df[col + '_z']
    
    return z_scores, df