import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Import dedicated modular engines
from modules.data_loader import load_dataset, detect_outliers_iqr, generate_frequency_distribution
from modules.descriptive_stats import compute_ungrouped_stats, compute_grouped_stats
from modules.extreme_value_analysis import fit_normal_distribution, calculate_exceedance_probability, get_standard_imd_threshold_risks, generate_normal_curve_data
from modules.bayesian_inference import compute_joint_marginal_tables, compute_bayes_sensor_update
from modules.time_series_process import compute_autocorrelation, analyze_stationarity, detect_heatwave_streaks
from modules.decision_engine import evaluate_heatwave_risk

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Heatwave Early Warning System | STAT-AI IA1",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Modern Custom Styling ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #F8FAFC 0%, #EDF2F7 100%);
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .formula-box {
        background-color: #F8FAFC;
        border-left: 4px solid #3B82F6;
        padding: 1rem 1.2rem;
        border-radius: 6px;
        margin: 0.8rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar: Ingestion & Live Simulation ---
st.sidebar.image("https://img.icons8.com/fluency/96/temperature.png", width=64)
st.sidebar.title("🌡️ Control Center")
st.sidebar.caption("S.Y. B.Tech | Statistical Methods & Probability (IA-1)")

# Dataset Loader
DATA_FILE_DEFAULT = Path("data/imd_heatwave_mumbai_maharashtra.csv")
uploaded_file = st.sidebar.file_uploader("Upload Weather CSV", type=['csv'])

if uploaded_file is not None:
    df_raw = load_dataset(uploaded_file)
    st.sidebar.success("Custom dataset loaded!")
elif DATA_FILE_DEFAULT.exists():
    df_raw = load_dataset(DATA_FILE_DEFAULT)
else:
    st.sidebar.error("Default dataset missing. Please upload a CSV.")
    st.stop()

# Interactive What-If Simulation Sliders
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Live What-If Simulator")
st.sidebar.caption("Simulate real-time temperature spike scenarios:")

sim_temp_offset = st.sidebar.slider("Temperature Offset (ΔT °C)", -5.0, 8.0, 0.0, 0.5)
sim_humidity_override = st.sidebar.slider("Relative Humidity (%)", 20, 95, int(df_raw['Relative_Humidity_Pct'].iloc[-1]))

# Create simulated current values based on the latest observation
last_obs = df_raw.iloc[-1].copy()
current_max_temp = float(last_obs['Max_Temp_C']) + sim_temp_offset
current_humidity = float(sim_humidity_override)

# Compute simulated Heat Index (Rothfusz equation)
def calc_heat_index(t, rh):
    tf = t * 9/5 + 32
    hif = 0.5 * (tf + 61.0 + ((tf - 68.0) * 1.2) + (rh * 0.094))
    if hif >= 80:
        hif = (-42.379 + 2.04901523*tf + 10.14333127*rh - 0.22475541*tf*rh
               - 0.00683783*tf*tf - 0.05481717*rh*rh + 0.00122874*tf*tf*rh
               + 0.00085282*tf*rh*rh - 0.00000199*tf*tf*rh*rh)
    return round((hif - 32) * 5/9, 1)

current_heat_index = calc_heat_index(current_max_temp, current_humidity)

# Sidebar Team Attribution
st.sidebar.markdown("---")
st.sidebar.subheader("👥 6-Member Roster")
team_members = [
    ("Tab 1: Member 1", "Data & Frequency Tables", "data_loader.py"),
    ("Tab 2: Member 2", "Descriptive Stats & Dispersion", "descriptive_stats.py"),
    ("Tab 3: Member 3", "Extreme Value & Normal Dist", "extreme_value_analysis.py"),
    ("Tab 4: Member 4", "Conditional Prob & Bayes", "bayesian_inference.py"),
    ("Tab 5: Member 5", "Random Process & Time Series", "time_series_process.py"),
    ("Tab 6: Member 6 (Lead)", "AI Decision Engine & UI", "decision_engine.py & app.py")
]
for m, role, mod in team_members:
    st.sidebar.markdown(f"**{m}**: {role} `({mod})`")

# --- Core Calculations ---
stat_summary = compute_ungrouped_stats(df_raw['Max_Temp_C'])
norm_params = fit_normal_distribution(df_raw['Max_Temp_C'])
prob_exceed_40 = calculate_exceedance_probability(40.0, norm_params['mu'], norm_params['sigma'])
prob_exceed_42 = calculate_exceedance_probability(42.0, norm_params['mu'], norm_params['sigma'])
prob_exceed_sim = calculate_exceedance_probability(current_max_temp, norm_params['mu'], norm_params['sigma'])

streak_df = detect_heatwave_streaks(df_raw, threshold=40.0)
current_streak = streak_df.iloc[-1]['Duration (Days)'] if not streak_df.empty else 0

# AI Decision evaluation
ai_decision = evaluate_heatwave_risk(
    current_temp=current_max_temp,
    prob_exceed_40=prob_exceed_40['probability'],
    prob_exceed_42=prob_exceed_42['probability'],
    heat_index=current_heat_index,
    streak_days=int(current_streak)
)

# --- Header Section ---
st.markdown("<div class='main-title'>☀️ AI-Based Heatwave Monitoring & Early Warning System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Case Study 1 | Statistical Investigation & Interactive Demonstration | IA-1 Assessment</div>", unsafe_allow_html=True)

# --- 6 DEDICATED TABS FOR THE 6 MEMBERS ---
tabs = st.tabs([
    "📊 Tab 1: Member 1 (Data & Frequency)",
    "📐 Tab 2: Member 2 (Descriptive Stats)",
    "🔔 Tab 3: Member 3 (Normal Distribution)",
    "🎲 Tab 4: Member 4 (Bayesian Inference)",
    "⏳ Tab 5: Member 5 (Random Process)",
    "🚨 Tab 6: Member 6 (AI Decision Engine)"
])

# ==========================================
# TAB 1: MEMBER 1 - DATA ENGINEERING & FREQUENCY TABLES
# ==========================================
with tabs[0]:
    st.markdown("### 📊 Tab 1: Data Hygiene, Ingestion & Frequency Distribution")
    st.caption("Responsible: **Member 1 (Data Engineer & Ingestion Lead)** | Presentation Slot: **Min 0:00 – 1:00**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("1. Data Hygiene & Outlier Detection")
        outliers = detect_outliers_iqr(df_raw['Max_Temp_C'])
        
        st.markdown(f"""
        - **Total Observations ($N$):** {len(df_raw)} days (IMD Maharashtra Records)
        - **First Quartile ($Q_1$):** {outliers['q1']} °C
        - **Third Quartile ($Q_3$):** {outliers['q3']} °C
        - **Interquartile Range ($IQR$):** {outliers['iqr']} °C
        - **Lower Fence ($Q_1 - 1.5 \\times IQR$):** {outliers['lower_bound']} °C
        - **Upper Fence ($Q_3 + 1.5 \\times IQR$):** {outliers['upper_bound']} °C
        - **Identified Outliers:** {outliers['outlier_count']} observations {outliers['outlier_values']}
        """)
        
        st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
        st.latex(r"IQR = Q_3 - Q_1")
        st.latex(rf"\text{{IQR}} = {outliers['q3']} - {outliers['q1']} = {outliers['iqr']}^\circ\text{{C}}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.subheader("2. Continuous Frequency Distribution Table")
        num_bins = st.slider("Select Number of Class Intervals (Sturges' Rule)", 5, 10, 7)
        freq_df, bin_edges = generate_frequency_distribution(df_raw['Max_Temp_C'], num_bins=num_bins)
        
        st.dataframe(freq_df, use_container_width=True)
        
        st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
        st.markdown(rf"**Verification:** $\sum f_i = {freq_df['Frequency (fi)'].sum()}$ (Matches $N = {len(df_raw)}$) | $\sum f_i x_i = {freq_df['fi * xi'].sum():.2f}$")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("3. Graphical Representations: Histogram & Ogive Curve")
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        fig_hist = px.histogram(
            df_raw, x="Max_Temp_C", nbins=num_bins,
            title="Histogram of Daily Maximum Temperature",
            labels={'Max_Temp_C': 'Max Temperature (°C)'},
            color_discrete_sequence=['#3B82F6']
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with g_col2:
        fig_ogive = go.Figure()
        fig_ogive.add_trace(go.Scatter(
            x=freq_df['Upper Limit (U)'], y=freq_df['Cumulative Freq (cf)'],
            mode='lines+markers', name='Less-than Ogive',
            line=dict(color='#10B981', width=2)
        ))
        fig_ogive.update_layout(
            title="Cumulative Frequency (Less-than Ogive) Curve",
            xaxis_title="Upper Class Boundary (°C)", yaxis_title="Cumulative Frequency (cf)"
        )
        st.plotly_chart(fig_ogive, use_container_width=True)

# ==========================================
# TAB 2: MEMBER 2 - DESCRIPTIVE STATS & DISPERSION
# ==========================================
with tabs[1]:
    st.markdown("### 📐 Tab 2: Central Tendency & Measures of Dispersion")
    st.caption("Responsible: **Member 2 (Descriptive Statistics Lead)** | Presentation Slot: **Min 1:00 – 2:00**")
    
    grouped_stats = compute_grouped_stats(freq_df)
    
    d_c1, d_c2, d_c3, d_c4 = st.columns(4)
    with d_c1:
        st.metric("Sample Mean (x̄)", f"{stat_summary['mean']} °C", f"Grouped: {grouped_stats['grouped_mean']} °C")
    with d_c2:
        st.metric("Median (Md)", f"{stat_summary['median']} °C", f"Grouped: {grouped_stats['grouped_median']} °C")
    with d_c3:
        st.metric("Std Deviation (s)", f"{stat_summary['std_dev']} °C", f"Variance: {stat_summary['variance']}")
    with d_c4:
        st.metric("Coeff of Variation (CV)", f"{stat_summary['cv']} %", "Thermal Volatility")

    st.markdown("---")
    st.subheader("Step-by-Step Numerical Derivations (Manual Substitution)")
    
    s_col1, s_col2 = st.columns(2)
    
    with s_col1:
        st.markdown("**1. Sample Mean Calculation:**")
        st.latex(stat_summary['steps']['mean_formula'])
        st.latex(stat_summary['steps']['mean_sub'])
        
        st.markdown("**2. Sample Variance Calculation (Bessel's Correction N-1):**")
        st.latex(stat_summary['steps']['variance_formula'])
        st.latex(stat_summary['steps']['variance_sub'])

    with s_col2:
        st.markdown("**3. Standard Deviation Calculation:**")
        st.latex(stat_summary['steps']['std_formula'])
        st.latex(stat_summary['steps']['std_sub'])
        
        st.markdown("**4. Coefficient of Variation (CV) Calculation:**")
        st.latex(stat_summary['steps']['cv_formula'])
        st.latex(stat_summary['steps']['cv_sub'])
        
    st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
    st.markdown(rf"""
    **Engineering Interpretation:**
    - A Coefficient of Variation of **{stat_summary['cv']}%** indicates relative thermal stability in the baseline, but the spread ($s = {stat_summary['std_dev']}^\circ\text{{C}}$) is large enough that a positive $2\sigma$ departure pushes the region straight into severe heatwave territory.
    - Grouped Mean (${grouped_stats['grouped_mean']}^\circ\text{{C}}$) closely matches Ungrouped Mean (${stat_summary['mean']}^\circ\text{{C}}$), verifying minimal grouping error.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.subheader("Box-and-Whisker Dispersion Diagram")
    fig_box = px.box(df_raw, y="Max_Temp_C", points="all", title="Temperature Dispersion & Quartile Distribution")
    st.plotly_chart(fig_box, use_container_width=True)

# ==========================================
# TAB 3: MEMBER 3 - EXTREME VALUE & NORMAL DISTRIBUTION
# ==========================================
with tabs[2]:
    st.markdown("### 🔔 Tab 3: Variability & Extreme Temperature Analysis")
    st.caption("Responsible: **Member 3 (Probability & Normal Distribution Specialist)** | Presentation Slot: **Min 2:00 – 3:15**")
    
    p_col1, p_col2 = st.columns([1, 2])
    
    with p_col1:
        st.subheader("1. Gaussian Distribution Parameters")
        st.markdown(rf"""
        - **Fitted Mean ($\mu$):** {norm_params['mu']} °C
        - **Fitted Std Dev ($\sigma$):** {norm_params['sigma']} °C
        - **Variance ($\sigma^2$):** {norm_params['variance']} (°C)²
        """)
        
        st.markdown("---")
        st.subheader("2. Interactive Threshold Probability")
        user_thresh = st.slider("Select Temperature Threshold (°C)", 36.0, 48.0, 40.0, 0.5)
        user_res = calculate_exceedance_probability(user_thresh, norm_params['mu'], norm_params['sigma'])
        
        st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
        st.latex(user_res['steps']['z_formula'])
        st.latex(user_res['steps']['z_sub'])
        st.latex(user_res['steps']['prob_formula'])
        st.latex(user_res['steps']['prob_sub'])
        st.markdown("</div>", unsafe_allow_html=True)

    with p_col2:
        st.subheader("3. Fitted Normal Distribution & Critical Tail Area")
        x_norm, y_norm = generate_normal_curve_data(norm_params['mu'], norm_params['sigma'])
        
        fig_norm = go.Figure()
        fig_norm.add_trace(go.Scatter(
            x=x_norm, y=y_norm, mode='lines', name=f"N({norm_params['mu']}, {norm_params['sigma']}²)",
            line=dict(color='#2563EB', width=2.5)
        ))
        
        mask = x_norm >= user_thresh
        if np.any(mask):
            fig_norm.add_trace(go.Scatter(
                x=np.concatenate([[user_thresh], x_norm[mask], [x_norm[mask][-1]]]),
                y=np.concatenate([[0], y_norm[mask], [0]]),
                fill='toself', fillcolor='rgba(220, 38, 38, 0.4)',
                line=dict(color='rgba(220, 38, 38, 0)'),
                name=f"P(T ≥ {user_thresh}°C) = {user_res['percentage']}%"
            ))
            
        fig_norm.add_vline(x=user_thresh, line_dash="dash", line_color="#DC2626")
        fig_norm.update_layout(
            title=f"Normal Curve PDF (Shaded Critical Area = {user_res['percentage']}%)",
            xaxis_title="Maximum Temperature (°C)", yaxis_title="Probability Density f(x)"
        )
        st.plotly_chart(fig_norm, use_container_width=True)

    st.subheader("4. Standard IMD Operational Risk Probabilities")
    std_risks = get_standard_imd_threshold_risks(norm_params['mu'], norm_params['sigma'])
    risk_summary_df = pd.DataFrame([{
        'Threshold Level': f"{r['threshold']} °C",
        'Z-Score': r['z_score'],
        'P(X ≥ T)': f"{r['probability']:.4f}",
        'Probability (%)': f"{r['percentage']}%",
        'Risk Category': 'Moderate' if r['threshold'] < 40 else 'Severe Heatwave' if r['threshold'] < 45 else 'Extreme Catastrophe'
    } for r in std_risks])
    st.table(risk_summary_df)

# ==========================================
# TAB 4: MEMBER 4 - BAYESIAN INFERENCE & CONDITIONAL PROBABILITY
# ==========================================
with tabs[3]:
    st.markdown("### 🎲 Tab 4: Conditional Probability & Bayesian Heatwave Inference")
    st.caption("Responsible: **Member 4 (Conditional Probability & Bayes' Inference Lead)** | Presentation Slot: **Min 3:15 – 4:30**")
    
    b_col1, b_col2 = st.columns(2)
    
    with b_col1:
        st.subheader("1. Joint & Marginal Contingency Table")
        jm_data = compute_joint_marginal_tables(df_raw)
        st.markdown("**Contingency Table: Counts**")
        st.dataframe(jm_data['cross_tab'], use_container_width=True)
        
        st.markdown("**Joint & Marginal Probabilities (%)**")
        st.dataframe(jm_data['prob_tab'], use_container_width=True)
        
        st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
        st.latex(r"P(\text{Heatwave} \mid \text{High Humidity}) = \frac{n(\text{Heatwave} \cap \text{High Hum})}{n(\text{High Hum})}")
        st.latex(rf"= \frac{{{jm_data['n_both']}}}{{{jm_data['n_high_hum']}}} = {jm_data['cond_prob']:.4f}\ ({jm_data['cond_prob']*100:.1f}\%)")
        st.markdown("</div>", unsafe_allow_html=True)

    with b_col2:
        st.subheader("2. Bayes' Theorem: AI/IoT Sensor Belief Update")
        st.write("An IoT Weather Station flags a Heatwave Alert ($S$). What is the posterior belief of a true heatwave ($H$)?")
        
        sens = st.slider("Sensor Sensitivity P(S | H) (True Positive Rate)", 0.70, 0.99, 0.92, 0.01)
        fpr = st.slider("Sensor False Alarm Rate P(S | ~H)", 0.01, 0.30, 0.08, 0.01)
        
        prior_h = jm_data['prior_heatwave']
        bayes_res = compute_bayes_sensor_update(prior_h, sensitivity=sens, false_positive_rate=fpr)
        
        st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
        st.latex(bayes_res['steps']['bayes_formula'])
        st.latex(bayes_res['steps']['bayes_sub'])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.success(f"**Bayesian Result:** Given a sensor alarm, posterior belief jumps from prior **{prior_h*100:.1f}%** to **{bayes_res['posterior_pct']}%**!")

    st.markdown("---")
    st.subheader("3. 2D Joint Distribution Heatmap (Temperature vs Relative Humidity)")
    fig_joint = px.density_heatmap(
        df_raw, x="Max_Temp_C", y="Relative_Humidity_Pct",
        nbinsx=15, nbinsy=15, color_continuous_scale="Viridis",
        title="Joint Density of Temperature vs Humidity"
    )
    st.plotly_chart(fig_joint, use_container_width=True)

# ==========================================
# TAB 5: MEMBER 5 - TIME SERIES & RANDOM PROCESS
# ==========================================
with tabs[4]:
    st.markdown("### ⏳ Tab 5: Temperature as a Random Process & Autocorrelation")
    st.caption("Responsible: **Member 5 (Time Series & Random Process Lead)** | Presentation Slot: **Min 4:30 – 5:30**")
    
    acf_df, ci_bound, acf_steps = compute_autocorrelation(df_raw['Max_Temp_C'], max_lags=7)
    stat_eval = analyze_stationarity(df_raw, window=7)
    
    t_c1, t_c2 = st.columns([1, 2])
    
    with t_c1:
        st.subheader("1. Sample Autocorrelation Function (ACF)")
        st.dataframe(acf_df, use_container_width=True)
        
        st.markdown("<div class='formula-box'>", unsafe_allow_html=True)
        st.latex(acf_steps['acf_formula'])
        st.latex(acf_steps['lag1_sub'])
        st.latex(acf_steps['ci_formula'])
        st.markdown("</div>", unsafe_allow_html=True)

    with t_c2:
        st.subheader("2. Autocorrelation Correlogram (Lags 1 to 7)")
        fig_acf = go.Figure()
        fig_acf.add_trace(go.Bar(
            x=acf_df['Lag (Days)'], y=acf_df['Autocorrelation (rk)'],
            name='Sample Autocorrelation r_k', marker_color='#3B82F6', width=0.4
        ))
        fig_acf.add_hline(y=ci_bound, line_dash="dash", line_color="#EF4444", annotation_text="+95% CI")
        fig_acf.add_hline(y=-ci_bound, line_dash="dash", line_color="#EF4444", annotation_text="-95% CI")
        fig_acf.add_hline(y=0.0, line_color="#94A3B8")
        
        fig_acf.update_layout(
            xaxis_title="Lag k (Days)", yaxis_title="Autocorrelation Coefficient (rk)",
            yaxis_range=[-0.4, 1.0], height=320
        )
        st.plotly_chart(fig_acf, use_container_width=True)

    st.markdown("---")
    st.subheader("3. Weak Stationarity Analysis & Multi-Day Persistence")
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        st.markdown(f"""
        - **7-Day Rolling Mean Spread:** {stat_eval['mean_diff']} °C
        - **7-Day Rolling Std Dev Spread:** {stat_eval['std_diff']} °C
        - **Statistical Evaluation:** **{stat_eval['judgment']}**
        """)
        st.markdown("**Detected Heatwave Streaks (≥ 40°C for ≥ 2 Days):**")
        st.dataframe(streak_df, use_container_width=True)
        
    with s_col2:
        fig_roll = go.Figure()
        fig_roll.add_trace(go.Scatter(x=df_raw['Date'], y=df_raw['Max_Temp_C'], mode='lines', name='Daily Max Temp', line=dict(color='#CBD5E1', width=1)))
        fig_roll.add_trace(go.Scatter(x=df_raw['Date'], y=stat_eval['rolling_mean'], mode='lines', name='7-Day Rolling Mean', line=dict(color='#F97316', width=2.5)))
        fig_roll.update_layout(title="Stationarity Test: 7-Day Rolling Mean Drift", xaxis_title="Date", yaxis_title="Temp (°C)", height=280)
        st.plotly_chart(fig_roll, use_container_width=True)

# ==========================================
# TAB 6: MEMBER 6 - AI DECISION ENGINE, EARLY WARNING & REPORT
# ==========================================
with tabs[5]:
    st.markdown("### 🚨 Tab 6: AI Decision Engine & Early Warning System")
    st.caption("Responsible: **Member 6 (AI Decision Engine & UI Lead - You!)** | Presentation Slot: **Min 5:30 – 6:45**")
    
    # Alert Status Banner
    alert_box_html = f"""
    <div style="background-color: {ai_decision['color']}15; border: 2px solid {ai_decision['color']}; border-radius: 12px; padding: 1.2rem; margin-bottom: 1.5rem;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
                <span style="font-size: 0.9rem; font-weight: 700; color: {ai_decision['color']}; text-transform: uppercase; letter-spacing: 1px;">IMD AI Early Warning Protocol</span>
                <h2 style="margin: 0.2rem 0; color: {ai_decision['color']}; font-size: 1.8rem;">{ai_decision['tier']} ALERT: {ai_decision['title']}</h2>
            </div>
            <div style="font-size: 2.2rem;">
                {"🟢" if ai_decision['tier'] == "GREEN" else "🟡" if ai_decision['tier'] == "YELLOW" else "🟠" if ai_decision['tier'] == "ORANGE" else "🔴"}
            </div>
        </div>
        <p style="margin: 0.6rem 0 0 0; color: #334155; font-size: 1.05rem;"><strong>Statistical Rationale:</strong> {ai_decision['rationale']}</p>
    </div>
    """
    st.markdown(alert_box_html, unsafe_allow_html=True)
    
    # Metrics Row
    m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)
    with m_col1:
        st.metric("Simulated Max Temp", f"{current_max_temp:.1f} °C", f"{sim_temp_offset:+.1f} °C" if sim_temp_offset != 0 else None)
    with m_col2:
        st.metric("Apparent Heat Index", f"{current_heat_index:.1f} °C", f"RH {current_humidity:.0f}%")
    with m_col3:
        st.metric("P(T ≥ 40°C)", f"{prob_exceed_40['percentage']}%", "Normal Fit")
    with m_col4:
        st.metric("P(T ≥ 42°C)", f"{prob_exceed_42['percentage']}%", "Severe Tail")
    with m_col5:
        st.metric("Active Streak", f"{current_streak} Days", "≥ 40°C")
        
    st.markdown("---")
    
    # Layout: Chart + Municipal Action Directives
    c_left, c_right = st.columns([3, 2])
    
    with c_left:
        st.subheader("📈 Temperature Telemetry vs IMD Warning Thresholds")
        fig_ts = go.Figure()
        fig_ts.add_trace(go.Scatter(
            x=df_raw['Date'], y=df_raw['Max_Temp_C'],
            mode='lines+markers', name='Observed Max Temp',
            line=dict(color='#2563EB', width=2), marker=dict(size=5)
        ))
        fig_ts.add_trace(go.Scatter(
            x=df_raw['Date'], y=df_raw['Heat_Index_C'],
            mode='lines', name='NOAA Heat Index',
            line=dict(color='#DC2626', width=1.5, dash='dash')
        ))
        fig_ts.add_hline(y=40.0, line_dash="dot", line_color="#CA8A04", annotation_text="Heatwatch (40°C)", annotation_position="top left")
        fig_ts.add_hline(y=42.0, line_dash="dot", line_color="#EA580C", annotation_text="Severe Alert (42°C)", annotation_position="top left")
        fig_ts.add_hline(y=45.0, line_dash="dot", line_color="#DC2626", annotation_text="Extreme Emergency (45°C)", annotation_position="top left")
        fig_ts.update_layout(
            height=360, margin=dict(l=20, r=20, t=30, b=20),
            xaxis_title="Date", yaxis_title="Temperature (°C)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ts, use_container_width=True)
        
    with c_right:
        st.subheader("🏛️ Automated Engineering & Civil Directives")
        for act in ai_decision['actions']:
            st.markdown(f"- {act}")
            
    st.markdown("---")
    st.subheader("📑 Final Assessment Submission & Group Roster")
    
    team_table = pd.DataFrame([
        {"Tab": "Tab 1", "Member": "Member 1", "Role": "Data Engineering Lead", "Topic": "IQR Outliers, 7-Bin Frequency Table, Ogive", "Time": "0:00–1:00"},
        {"Tab": "Tab 2", "Member": "Member 2", "Role": "Descriptive Statistics Lead", "Topic": "Mean, Median, Variance, Std Dev, CV", "Time": "1:00–2:00"},
        {"Tab": "Tab 3", "Member": "Member 3", "Role": "Probability & Extreme Value Lead", "Topic": "Gaussian Fitting, Z-scores, P(T ≥ 40°C)", "Time": "2:00–3:15"},
        {"Tab": "Tab 4", "Member": "Member 4", "Role": "Bayesian Inference Specialist", "Topic": "Joint Tables, Conditional Prob, Bayes' Sensor Update", "Time": "3:15–4:30"},
        {"Tab": "Tab 5", "Member": "Member 5", "Role": "Time Series & Random Process Lead", "Topic": "Random Process, Autocorrelation ACF, Streaks", "Time": "4:30–5:30"},
        {"Tab": "Tab 6", "Member": "Member 6 (You)", "Role": "AI Decision Engine & UI Lead", "Topic": "AI Early Warning Matrix, Municipal Directives, Simulation", "Time": "5:30–6:45"}
    ])
    st.dataframe(team_table, use_container_width=True)
    
    report_text = f"""
================================================================================
STATISTICAL INVESTIGATION SHEET: CASE STUDY 1
AI-BASED HEATWAVE MONITORING AND EARLY WARNING SYSTEM
Somaiya Vidyavihar University | S.Y. B.Tech | IA-1 Assessment
================================================================================

1. PROBLEM STATEMENT:
To design an AI-supported statistical early warning system to monitor daily 
maximum temperatures and issue multi-tier municipal advisories (Green, Yellow, 
Orange, Red) before extreme heat events threaten public health.

2. DATASET DESCRIPTION:
- Source: India Meteorological Department (IMD) / data.gov.in
- Observations: {len(df_raw)} daily summer records
- Key Variables: Date, Max_Temp_C, Min_Temp_C, Relative_Humidity_Pct, Heat_Index_C

3. STATISTICAL SUMMARY & MATHEMATICAL RESULTS:
- Sample Mean (x̄): {stat_summary['mean']} °C
- Sample Median (Md): {stat_summary['median']} °C
- Sample Standard Deviation (s): {stat_summary['std_dev']} °C
- Coefficient of Variation (CV): {stat_summary['cv']} %
- Fitted Normal Distribution: N({norm_params['mu']}, {norm_params['sigma']}^2)
- Exceedance Probability P(T >= 40°C): {prob_exceed_40['percentage']}%
- Exceedance Probability P(T >= 42°C): {prob_exceed_42['percentage']}%
- Lag-1 Autocorrelation (r1): {acf_df.iloc[0]['Autocorrelation (rk)']} (95% CI: +/- {ci_bound})

4. AI / ENGINEERING DECISION:
- Current AI Alert Level: {ai_decision['tier']} ({ai_decision['title']})
- Directives:
{chr(10).join(['  * ' + a for a in ai_decision['actions']])}

5. LIMITATIONS:
- Gaussian assumption slightly underestimates the heavy positive kurtosis of extreme heatwaves.
- Meteorological processes exhibit non-stationarity across seasonal transitions.
================================================================================
"""
    st.download_button(
        label="📄 Download Official Statistical Investigation Sheet (.txt)",
        data=report_text,
        file_name="G1_HeatwaveMonitoring_StatAI_IA1_Report.txt",
        mime="text/plain"
    )
