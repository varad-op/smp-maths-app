"""
Module 3: Variability & Extreme Temperature Analysis
Owned by: Member 3 (Probability & Normal Distribution Specialist)
Topic: Normal Distribution, Z-score, Tail Exceedance Probability, Extreme Heat Risk
"""
import numpy as np
from scipy import stats

def fit_normal_distribution(series):
    """Estimate parameters mu and sigma of normal distribution."""
    mu = float(series.mean())
    sigma = float(series.std(ddof=1))
    return {
        'mu': round(mu, 2),
        'sigma': round(sigma, 2),
        'variance': round(sigma ** 2, 4)
    }

def calculate_exceedance_probability(threshold, mu, sigma):
    """
    Calculate Z-score and P(X >= threshold) using Standard Normal CDF.
    Z = (X - mu) / sigma
    P(X >= threshold) = 1 - Phi(Z)
    """
    z_score = (threshold - mu) / sigma
    prob_exceed = 1.0 - stats.norm.cdf(z_score)
    pct_exceed = prob_exceed * 100.0
    
    steps = {
        'z_formula': r"Z = \frac{X - \mu}{\sigma}",
        'z_sub': rf"Z = \frac{{{threshold:.1f} - {mu:.2f}}}{{{sigma:.2f}}} = {z_score:.4f}",
        'prob_formula': r"P(X \ge T) = 1 - \Phi(Z) = \int_{T}^{\infty} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} dx",
        'prob_sub': rf"P(X \ge {threshold:.1f}^\circ\text{{C}}) = 1 - \Phi({z_score:.2f}) = {prob_exceed:.4f}\ ({pct_exceed:.2f}\%)"
    }
    
    return {
        'threshold': threshold,
        'z_score': round(z_score, 4),
        'probability': round(prob_exceed, 4),
        'percentage': round(pct_exceed, 2),
        'steps': steps
    }

def get_standard_imd_threshold_risks(mu, sigma):
    """Compute probabilities for key IMD heatwave thresholds: 38C, 40C, 42C, 45C."""
    thresholds = [38.0, 40.0, 42.0, 45.0]
    results = []
    for t in thresholds:
        res = calculate_exceedance_probability(t, mu, sigma)
        results.append(res)
    return results

def generate_normal_curve_data(mu, sigma, num_points=250):
    """Generate x and y coordinates for Normal Distribution plotting."""
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, num_points)
    y = stats.norm.pdf(x, mu, sigma)
    return x, y
