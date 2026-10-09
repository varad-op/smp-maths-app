"""
Module 1: Data Engineering & Preprocessing
Owned by: Member 1 (Data Engineer & Ingestion Lead)
Topic: Data hygiene, Outliers (IQR), Frequency Distribution, Classification & Tabulation
"""
import pandas as pd
import numpy as np

def load_dataset(file_path_or_buffer):
    """Load meteorological dataset and perform type validation."""
    if file_path_or_buffer is None:
        return None
    df = pd.read_csv(file_path_or_buffer)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    return df

def detect_outliers_iqr(series):
    """Detect statistical outliers using Interquartile Range (IQR) method."""
    q1 = float(series.quantile(0.25))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    return {
        'q1': round(q1, 2),
        'q3': round(q3, 2),
        'iqr': round(iqr, 2),
        'lower_bound': round(lower_bound, 2),
        'upper_bound': round(upper_bound, 2),
        'outlier_count': len(outliers),
        'outlier_values': [round(x, 2) for x in outliers.tolist()]
    }

def generate_frequency_distribution(series, num_bins=7):
    """
    Generate continuous frequency distribution table.
    Computes: Class Intervals, Class Marks (xi), Frequency (fi),
    Cumulative Frequency (cf), Relative Frequency (%), fi*xi, fi*xi^2.
    """
    min_val = float(np.floor(series.min()))
    max_val = float(np.ceil(series.max()))
    bins = np.linspace(min_val, max_val, num_bins + 1)
    
    labels = [f"{bins[i]:.1f} - {bins[i+1]:.1f}" for i in range(len(bins)-1)]
    categories = pd.cut(series, bins=bins, labels=labels, include_lowest=True)
    
    freq_series = categories.value_counts(sort=False)
    
    table_rows = []
    cum_freq = 0
    total_n = len(series)
    
    for i, (interval_label, count) in enumerate(freq_series.items()):
        lower = float(bins[i])
        upper = float(bins[i+1])
        midpoint = (lower + upper) / 2.0
        cum_freq += int(count)
        rel_freq = (int(count) / total_n) * 100.0
        fi_xi = int(count) * midpoint
        fi_xi2 = int(count) * (midpoint ** 2)
        
        table_rows.append({
            'Class Interval (°C)': interval_label,
            'Lower Limit (L)': round(lower, 1),
            'Upper Limit (U)': round(upper, 1),
            'Class Mark (xi)': round(midpoint, 2),
            'Frequency (fi)': int(count),
            'Cumulative Freq (cf)': int(cum_freq),
            'Relative Freq (%)': round(rel_freq, 2),
            'fi * xi': round(fi_xi, 2),
            'fi * xi^2': round(fi_xi2, 2)
        })
        
    freq_df = pd.DataFrame(table_rows)
    return freq_df, bins
