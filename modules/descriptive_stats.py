"""
Module 2: Descriptive Statistics & Dispersion
Owned by: Member 2 (Descriptive Statistics Lead)
Topic: Mean, Median, Mode, Variance, Standard Deviation, Coefficient of Variation
"""
import numpy as np
import pandas as pd

def compute_ungrouped_stats(series):
    """
    Compute rigorous descriptive statistics for ungrouped temperature data.
    Returns calculated values and explicit step-by-step formula strings.
    """
    n = len(series)
    sum_x = float(series.sum())
    mean_val = sum_x / n
    median_val = float(series.median())
    mode_val = float(series.mode().iloc[0]) if not series.mode().empty else mean_val
    
    range_val = float(series.max() - series.min())
    sum_sq_diff = float(((series - mean_val) ** 2).sum())
    variance_val = sum_sq_diff / (n - 1)  # sample variance
    std_val = float(np.sqrt(variance_val))
    cv_val = (std_val / mean_val) * 100.0  # Coefficient of Variation
    
    steps = {
        'mean_formula': r"\bar{x} = \frac{\sum_{i=1}^N x_i}{N}",
        'mean_sub': rf"\bar{x} = \frac{{{sum_x:.2f}}}{{{n}}} = {mean_val:.2f}^\circ\text{{C}}",
        'variance_formula': r"s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}",
        'variance_sub': rf"s^2 = \frac{{{sum_sq_diff:.2f}}}{{{n} - 1}} = \frac{{{sum_sq_diff:.2f}}}{{{n - 1}}} = {variance_val:.4f}\ (^\circ\text{{C}})^2",
        'std_formula': r"s = \sqrt{s^2}",
        'std_sub': rf"s = \sqrt{{{variance_val:.4f}}} = {std_val:.2f}^\circ\text{{C}}",
        'cv_formula': r"CV = \left( \frac{s}{\bar{x}} \right) \times 100\%",
        'cv_sub': rf"CV = \left( \frac{{{std_val:.2f}}}{{{mean_val:.2f}}} \right) \times 100\% = {cv_val:.2f}\%"
    }
    
    return {
        'n': n,
        'mean': round(mean_val, 2),
        'median': round(median_val, 2),
        'mode': round(mode_val, 2),
        'min': round(float(series.min()), 2),
        'max': round(float(series.max()), 2),
        'range': round(range_val, 2),
        'variance': round(variance_val, 4),
        'std_dev': round(std_val, 2),
        'cv': round(cv_val, 2),
        'steps': steps
    }

def compute_grouped_stats(freq_df):
    """
    Compute grouped statistics from Frequency Distribution Table.
    Grouped Mean = sum(fi * xi) / sum(fi)
    Grouped Median = L + ((N/2 - cf) / f) * h
    Grouped Mode = L + ((f1 - f0) / (2f1 - f0 - f2)) * h
    """
    total_n = int(freq_df['Frequency (fi)'].sum())
    sum_fi_xi = float(freq_df['fi * xi'].sum())
    grouped_mean = sum_fi_xi / total_n
    
    # Grouped Median
    half_n = total_n / 2.0
    med_idx = freq_df[freq_df['Cumulative Freq (cf)'] >= half_n].index[0]
    med_row = freq_df.iloc[med_idx]
    
    L_med = med_row['Lower Limit (L)']
    h_med = med_row['Upper Limit (U)'] - med_row['Lower Limit (L)']
    f_med = med_row['Frequency (fi)']
    cf_prev = freq_df.iloc[med_idx - 1]['Cumulative Freq (cf)'] if med_idx > 0 else 0
    
    grouped_median = L_med + ((half_n - cf_prev) / f_med) * h_med
    
    # Grouped Mode (Modal Class has highest frequency)
    modal_idx = freq_df['Frequency (fi)'].idxmax()
    modal_row = freq_df.iloc[modal_idx]
    
    L_mod = modal_row['Lower Limit (L)']
    h_mod = modal_row['Upper Limit (U)'] - modal_row['Lower Limit (L)']
    f1 = modal_row['Frequency (fi)']
    f0 = freq_df.iloc[modal_idx - 1]['Frequency (fi)'] if modal_idx > 0 else 0
    f2 = freq_df.iloc[modal_idx + 1]['Frequency (fi)'] if modal_idx < len(freq_df) - 1 else 0
    
    denom = (2 * f1 - f0 - f2)
    grouped_mode = L_mod + ((f1 - f0) / denom) * h_mod if denom != 0 else L_mod
    
    steps = {
        'grouped_mean_sub': rf"\bar{{x}}_{{grouped}} = \frac{{\sum f_i x_i}}{{\sum f_i}} = \frac{{{sum_fi_xi:.2f}}}{{{total_n}}} = {grouped_mean:.2f}^\circ\text{{C}}",
        'grouped_median_sub': rf"M_d = L + \left[ \frac{{\frac{{N}}{{2}} - cf_{{prev}}}}{{f}} \right] \cdot h = {L_med:.1f} + \left[ \frac{{{half_n:.1f} - {cf_prev}}}{{{f_med}}} \right] \cdot {h_med:.1f} = {grouped_median:.2f}^\circ\text{{C}}",
        'grouped_mode_sub': rf"M_o = L + \left[ \frac{{f_1 - f_0}}{{2f_1 - f_0 - f_2}} \right] \cdot h = {L_mod:.1f} + \left[ \frac{{{f1} - {f0}}}{{2({f1}) - {f0} - {f2}}} \right] \cdot {h_mod:.1f} = {grouped_mode:.2f}^\circ\text{{C}}"
    }
    
    return {
        'grouped_mean': round(grouped_mean, 2),
        'grouped_median': round(grouped_median, 2),
        'grouped_mode': round(grouped_mode, 2),
        'steps': steps
    }
