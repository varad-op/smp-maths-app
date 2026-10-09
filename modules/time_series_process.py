"""
Module 5: Temperature as a Random Process
Owned by: Member 5 (Time Series & Random Process Lead)
Topic: Random Process, Stationarity, Autocorrelation Function (ACF), Heatwave Streaks
"""
import numpy as np
import pandas as pd

def compute_autocorrelation(series, max_lags=7):
    """
    Compute sample autocorrelation coefficients r_k for lags k = 1 to max_lags.
    r_k = sum((X_t - mean) * (X_{t+k} - mean)) / sum((X_t - mean)^2)
    Also computes 95% Bartlett confidence bounds: +/- 1.96 / sqrt(N).
    """
    n = len(series)
    mean_val = float(series.mean())
    diff = series - mean_val
    denominator = float((diff ** 2).sum())
    
    acf_values = []
    lags = list(range(1, max_lags + 1))
    
    for k in lags:
        numerator = float((diff.iloc[:-k].values * diff.iloc[k:].values).sum())
        rk = numerator / denominator if denominator != 0 else 0.0
        acf_values.append(round(rk, 4))
        
    ci_bound = round(1.96 / np.sqrt(n), 4)
    
    steps = {
        'acf_formula': r"r_k = \frac{\sum_{t=1}^{N-k} (X_t - \bar{x})(X_{t+k} - \bar{x})}{\sum_{t=1}^N (X_t - \bar{x})^2}",
        'lag1_sub': rf"r_1 = \frac{{\text{{Cov}}(X_t, X_{{t+1}})}}{{s^2}} = {acf_values[0]:.4f}",
        'ci_formula': rf"\text{{95% CI Bounds}} = \pm \frac{{1.96}}{{\sqrt{{N}}}} = \pm \frac{{1.96}}{{\sqrt{{{n}}}}} = \pm {ci_bound:.4f}"
    }
    
    acf_df = pd.DataFrame({
        'Lag (Days)': lags,
        'Autocorrelation (rk)': acf_values,
        'Statistically Significant': [abs(val) > ci_bound for val in acf_values]
    })
    
    return acf_df, ci_bound, steps

def analyze_stationarity(df, window=7):
    """
    Evaluate weak stationarity by tracking rolling mean and rolling standard deviation.
    A weakly stationary process requires constant mean and constant variance over time.
    """
    series = df['Max_Temp_C']
    rolling_mean = series.rolling(window=window).mean()
    rolling_std = series.rolling(window=window).std()
    
    mean_diff = float(rolling_mean.max() - rolling_mean.min())
    std_diff = float(rolling_std.max() - rolling_std.min())
    
    stationarity_judgment = (
        "Non-Stationary (Seasonal Mean Drift present during summer heatwave spells)"
        if mean_diff > 3.0
        else "Locally Weakly Stationary"
    )
    
    return {
        'rolling_mean': rolling_mean,
        'rolling_std': rolling_std,
        'mean_diff': round(mean_diff, 2),
        'std_diff': round(std_diff, 2),
        'judgment': stationarity_judgment
    }

def detect_heatwave_streaks(df, threshold=40.0):
    """
    Detect continuous periods of consecutive days exceeding threshold.
    Returns streak metadata including longest duration.
    """
    is_hot = (df['Max_Temp_C'] >= threshold).astype(int)
    streaks = []
    current_streak = 0
    start_date = None
    
    for idx, row in df.iterrows():
        if row['Max_Temp_C'] >= threshold:
            if current_streak == 0:
                start_date = row['Date'].strftime('%Y-%m-%d')
            current_streak += 1
        else:
            if current_streak >= 2:
                streaks.append({
                    'Start Date': start_date,
                    'Duration (Days)': current_streak,
                    'Peak Temp (°C)': float(df.loc[idx - current_streak:idx - 1, 'Max_Temp_C'].max())
                })
            current_streak = 0
            
    # Check if ongoing at the end of series
    if current_streak >= 2:
        streaks.append({
            'Start Date': start_date,
            'Duration (Days)': current_streak,
            'Peak Temp (°C)': float(df.tail(current_streak)['Max_Temp_C'].max())
        })
        
    streak_df = pd.DataFrame(streaks) if streaks else pd.DataFrame(columns=['Start Date', 'Duration (Days)', 'Peak Temp (°C)'])
    return streak_df
