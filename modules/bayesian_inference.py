"""
Module 4: Conditional Probability & Bayesian Heatwave Inference
Owned by: Member 4 (Conditional Probability & Bayes' Inference Lead)
Topic: Joint & Marginal Tables, Conditional Probability, Bayes' Theorem, Heat Index
"""
import pandas as pd
import numpy as np

def compute_joint_marginal_tables(df):
    """
    Categorize temperature and humidity to compute Joint and Marginal Frequency Tables.
    Temperature: Moderate (<40C), Heatwave (>=40C)
    Humidity: Normal (<=60%), High (>60%)
    """
    temp_cat = df['Max_Temp_C'].apply(lambda t: 'Heatwave (>=40°C)' if t >= 40.0 else 'Moderate (<40°C)')
    hum_cat = df['Relative_Humidity_Pct'].apply(lambda h: 'High Hum (>60%)' if h > 60.0 else 'Normal Hum (<=60%)')
    
    cross_tab = pd.crosstab(temp_cat, hum_cat, margins=True, margins_name='Total')
    prob_tab = pd.crosstab(temp_cat, hum_cat, normalize=True, margins=True, margins_name='Total') * 100.0
    
    total_obs = len(df)
    n_heatwave_and_high_hum = cross_tab.loc['Heatwave (>=40°C)', 'High Hum (>60%)'] if ('Heatwave (>=40°C)' in cross_tab.index and 'High Hum (>60%)' in cross_tab.columns) else 0
    n_high_hum = cross_tab.loc['Total', 'High Hum (>60%)'] if 'High Hum (>60%)' in cross_tab.columns else 1
    
    cond_prob_heat_given_hum = (n_heatwave_and_high_hum / n_high_hum) if n_high_hum > 0 else 0.0
    
    n_heatwave = cross_tab.loc['Heatwave (>=40°C)', 'Total'] if 'Heatwave (>=40°C)' in cross_tab.index else 0
    prior_heatwave = (n_heatwave / total_obs) if total_obs > 0 else 0.0
    
    return {
        'cross_tab': cross_tab,
        'prob_tab': prob_tab.round(2),
        'total_obs': total_obs,
        'n_heatwave': n_heatwave,
        'n_high_hum': n_high_hum,
        'n_both': n_heatwave_and_high_hum,
        'cond_prob': round(cond_prob_heat_given_hum, 4),
        'prior_heatwave': round(prior_heatwave, 4)
    }

def compute_bayes_sensor_update(prior_h, sensitivity=0.92, false_positive_rate=0.08):
    """
    Apply Bayes' Theorem to update belief when an AI/IoT sensor triggers an alert (S).
    H: True Heatwave Occurrence
    S: Sensor Alarm Triggered
    P(H | S) = [P(S | H) * P(H)] / [P(S | H)*P(H) + P(S | ~H)*P(~H)]
    """
    prior_not_h = 1.0 - prior_h
    p_s_given_h = sensitivity
    p_s_given_not_h = false_positive_rate
    
    marginal_s = (p_s_given_h * prior_h) + (p_s_given_not_h * prior_not_h)
    posterior_h_given_s = (p_s_given_h * prior_h) / marginal_s if marginal_s > 0 else 0.0
    
    steps = {
        'bayes_formula': r"P(H \mid S) = \frac{P(S \mid H) \cdot P(H)}{P(S \mid H) \cdot P(H) + P(S \mid \neg H) \cdot P(\neg H)}",
        'bayes_sub': (
            rf"P(H \mid S) = \frac{{{p_s_given_h:.2f} \cdot {prior_h:.4f}}}"
            rf"{{{p_s_given_h:.2f} \cdot {prior_h:.4f} + {p_s_given_not_h:.2f} \cdot {prior_not_h:.4f}}} "
            rf"= \frac{{{p_s_given_h * prior_h:.4f}}}{{{marginal_s:.4f}}} = {posterior_h_given_s:.4f}\ ({posterior_h_given_s * 100:.2f}\%)"
        )
    }
    
    return {
        'prior_h': round(prior_h, 4),
        'sensitivity': round(sensitivity, 2),
        'false_positive': round(false_positive_rate, 2),
        'marginal_sensor_prob': round(marginal_s, 4),
        'posterior_prob': round(posterior_h_given_s, 4),
        'posterior_pct': round(posterior_h_given_s * 100, 2),
        'steps': steps
    }
