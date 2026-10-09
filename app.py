import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Heatwave Monitoring App | Team Starter Template",
    page_icon="🌡️",
    layout="wide"
)

st.title("☀️ AI-Based Heatwave Monitoring and Early Warning System")
st.caption("Case Study 1 | Statistical Methods and Probability (IA-1) | 6-Member Team Template")

# --- SHARED DATASET INGESTION ---
# Everyone uses this same dataframe (df) in their tabs!
DATA_PATH = "data/imd_heatwave_mumbai_maharashtra.csv"
try:
    df = pd.read_csv(DATA_PATH)
    st.sidebar.success(f"✅ Dataset Loaded: {len(df)} daily observations")
    st.sidebar.dataframe(df[['Date', 'Max_Temp_C', 'Relative_Humidity_Pct']].head(5))
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

st.sidebar.markdown("---")
st.sidebar.info("💡 **Instructions for Team Members:**\nFind your assigned tab below, look at the working example in **Tab 1**, and write your code inside your tab!")

# --- 6 DEDICATED TABS FOR THE 6 MEMBERS ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Tab 1: Member 1 (Data & Frequency)",
    "📐 Tab 2: Member 2 (Descriptive Stats)",
    "🔔 Tab 3: Member 3 (Normal Distribution)",
    "🎲 Tab 4: Member 4 (Bayesian Inference)",
    "⏳ Tab 5: Member 5 (Random Process)",
    "🚨 Tab 6: AI Decision Engine"
])

# ==============================================================================
# TAB 1: MEMBER 1 (WORKING EXAMPLE - SHOWS HOW TO WRITE CODE FOR STREAMLIT)
# ==============================================================================
with tab1:
    st.header("📊 Member 1: Data Ingestion & Frequency Distribution")
    st.write("**Assigned Role:** Data Engineering Lead | **Presentation Slot:** Min 0:00 – 1:00")
    
    st.markdown("### 🟢 Working Example (Use this as a reference for your tabs!):")
    
    # 1. How to show simple metric cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Observations (N)", value=len(df))
    with col2:
        st.metric(label="Minimum Temp Recorded", value=f"{df['Max_Temp_C'].min():.1f} °C")
    with col3:
        st.metric(label="Maximum Temp Recorded", value=f"{df['Max_Temp_C'].max():.1f} °C")
        
    st.markdown("---")
    
    # 2. How to show step-by-step LaTeX formulas (Professor requires this!)
    st.subheader("Step-by-Step Formula Example: Interquartile Range (IQR)")
    q1 = df['Max_Temp_C'].quantile(0.25)
    q3 = df['Max_Temp_C'].quantile(0.75)
    iqr = q3 - q1
    
    # Display formula using st.latex
    st.latex(r"IQR = Q_3 - Q_1")
    st.latex(rf"IQR = {q3:.2f}^\circ\text{{C}} - {q1:.2f}^\circ\text{{C}} = {iqr:.2f}^\circ\text{{C}}")
    
    st.markdown("---")
    
    # 3. How to create an interactive Plotly chart
    st.subheader("Interactive Plot Example: Temperature Histogram")
    fig = px.histogram(
        df, 
        x="Max_Temp_C", 
        nbins=7, 
        title="Frequency Distribution of Maximum Temperatures",
        labels={"Max_Temp_C": "Max Temperature (°C)"},
        color_discrete_sequence=['#3B82F6']
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("👆 **Member 1:** You can extend this tab by adding your 7-bin Frequency Table and Ogive curve.")


# ==============================================================================
# TAB 2: MEMBER 2 (DESCRIPTIVE STATISTICS & DISPERSION)
# ==============================================================================
with tab2:
    st.header("📐 Member 2: Descriptive Statistics & Measures of Dispersion")
    st.write("**Assigned Role:** Descriptive Statistics Lead | **Presentation Slot:** Min 1:00 – 2:00")
    
    st.markdown(r"""
    #### 📝 What Member 2 needs to put here:
    1. **Central Tendency:** Compute Mean ($\bar{x}$), Median ($M_d$), and Mode ($M_o$) of `df['Max_Temp_C']`.
    2. **Measures of Dispersion:** Compute Variance ($s^2$), Standard Deviation ($s$), and Coefficient of Variation ($CV = \frac{s}{\bar{x}} \times 100\%$).
    3. **Formulas:** Use `st.latex()` to display the formula and substituted numbers.
    4. **Chart:** Add a Box-and-Whisker plot using `px.box(df, y='Max_Temp_C')`.
    """)
    
    st.markdown("---")
    st.subheader("💻 Member 2 Starter Code Area:")
    
    # --- TODO: MEMBER 2 WRITE YOUR CALCULATIONS HERE ---
    sample_mean = df['Max_Temp_C'].mean()
    sample_std = df['Max_Temp_C'].std()
    cv_val = (sample_std / sample_mean) * 100
    
    # Example metric layout (customize this!)
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="Sample Mean (x̄)", value=f"{sample_mean:.2f} °C")
    with m_col2:
        st.metric(label="Sample Std Dev (s)", value=f"{sample_std:.2f} °C")
    with m_col3:
        st.metric(label="Coefficient of Variation (CV)", value=f"{cv_val:.2f} %")
        
    # TODO: Member 2, put your step-by-step LaTeX formulas here:
    # st.latex(r"\bar{x} = \frac{\sum x_i}{N}")
    # st.latex(r"s^2 = \frac{\sum (x_i - \bar{x})^2}{N - 1}")


# ==============================================================================
# TAB 3: MEMBER 3 (NORMAL DISTRIBUTION & EXTREME VALUES)
# ==============================================================================
with tab3:
    st.header("🔔 Member 3: Variability & Extreme Temperature Analysis")
    st.write("**Assigned Role:** Probability & Normal Distribution Lead | **Presentation Slot:** Min 2:00 – 3:15")
    
    st.markdown(r"""
    #### 📝 What Member 3 needs to put here:
    1. **Gaussian Parameters:** Fit Normal Distribution $\mathcal{N}(\mu, \sigma^2)$ using mean and standard deviation.
    2. **Z-Score Calculation:** Transform threshold temperatures into $Z$-scores using $Z = \frac{X - \mu}{\sigma}$.
    3. **Tail Exceedance Probabilities:** Calculate $P(X \ge 40^\circ\text{C})$ and $P(X \ge 42^\circ\text{C})$.
    4. **Interactive Slider & Bell Curve:** Let the user slide a temperature threshold and see the shaded probability area on the bell curve!
    """)
    
    st.markdown("---")
    st.subheader("💻 Member 3 Starter Code Area:")
    
    # --- TODO: MEMBER 3 WRITE YOUR CALCULATIONS HERE ---
    mu = df['Max_Temp_C'].mean()
    sigma = df['Max_Temp_C'].std()
    
    # Interactive threshold slider
    threshold_input = st.slider("Select Temperature Threshold (°C) for Risk Calculation:", 36.0, 48.0, 40.0, 0.5)
    z_score = (threshold_input - mu) / sigma
    
    st.write(f"**Calculated Z-Score for {threshold_input}°C:** `Z = {z_score:.4f}`")
    
    # TODO: Member 3, calculate P(X >= threshold) and plot the Normal Bell Curve using Plotly!


# ==============================================================================
# TAB 4: MEMBER 4 (CONDITIONAL PROBABILITY & BAYES' THEOREM)
# ==============================================================================
with tab4:
    st.header("🎲 Member 4: Conditional Probability & Bayesian Inference")
    st.write("**Assigned Role:** Bayesian Inference Specialist | **Presentation Slot:** Min 3:15 – 4:30")
    
    st.markdown(r"""
    #### 📝 What Member 4 needs to put here:
    1. **Joint & Marginal Contingency Table:** Create a 2x2 table of Temperature (Normal vs Heatwave) vs Humidity (Normal vs High).
    2. **Conditional Probability:** Calculate $P(\text{Heatwave} \mid \text{High Humidity})$.
    3. **Bayes' Theorem for IoT Sensor:** Update prior belief of heatwave when a weather sensor alarm triggers:
       $$P(H \mid S) = \\frac{P(S \mid H) P(H)}{P(S)}$$
    4. **Heatmap:** 2D density heatmap of Temperature vs Humidity.
    """)
    
    st.markdown("---")
    st.subheader("💻 Member 4 Starter Code Area:")
    
    # --- TODO: MEMBER 4 WRITE YOUR CALCULATIONS HERE ---
    # Example cross-tabulation:
    temp_category = df['Max_Temp_C'].apply(lambda t: 'Heatwave (>=40°C)' if t >= 40 else 'Normal (<40°C)')
    hum_category = df['Relative_Humidity_Pct'].apply(lambda h: 'High Hum (>60%)' if h > 60 else 'Normal Hum (<=60%)')
    contingency_table = pd.crosstab(temp_category, hum_category, margins=True)
    
    st.write("**Joint & Marginal Frequency Table:**")
    st.dataframe(contingency_table)
    
    # TODO: Member 4, write your conditional probability and Bayes' Theorem formulas and calculations here!


# ==============================================================================
# TAB 5: MEMBER 5 (TIME SERIES & RANDOM PROCESS)
# ==============================================================================
with tab5:
    st.header("⏳ Member 5: Temperature as a Random Process & Autocorrelation")
    st.write("**Assigned Role:** Time Series & Random Process Lead | **Presentation Slot:** Min 4:30 – 5:30")
    
    st.markdown(r"""
    #### 📝 What Member 5 needs to put here:
    1. **Random Process Representation:** Model daily temperature sequence as discrete time series $\{X_t\}$.
    2. **Autocorrelation Function (ACF):** Compute autocorrelation coefficients $r_1, r_2, \dots, r_7$ for lags 1 through 7 days.
    3. **95% Confidence Bounds:** Compute Bartlett's confidence bounds: $\pm \\frac{1.96}{\\sqrt{N}}$.
    4. **Stationarity & Streaks:** Show 7-day rolling mean and consecutive heatwave streaks (days $\ge 40^\circ\text{C}$).
    """)
    
    st.markdown("---")
    st.subheader("💻 Member 5 Starter Code Area:")
    
    # --- TODO: MEMBER 5 WRITE YOUR CALCULATIONS HERE ---
    # Example Lag-1 autocorrelation:
    lag1_autocorr = df['Max_Temp_C'].autocorr(lag=1)
    ci_bound = 1.96 / np.sqrt(len(df))
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Lag-1 Autocorrelation (r1)", value=f"{lag1_autocorr:.4f}")
    with col2:
        st.metric(label="95% Bartlett Confidence Bound", value=f"± {ci_bound:.4f}")
        
    # TODO: Member 5, plot the correlogram (ACF bar chart) and rolling mean graph here!


# ==============================================================================
# TAB 6: AI DECISION ENGINE & EARLY WARNING SYSTEM
# ==============================================================================
with tab6:
    st.header("🚨 AI Decision Engine & Early Warning System")
    st.caption("STAT-AI Real-Time Command Center | Automated Municipal Hazard Assessment & Resource Allocation")
    st.markdown("---")

    # 1. Microclimate Zone & 1-Click Historical Weather Presets
    ctrl_col1, ctrl_col2 = st.columns([1, 2])
    
    with ctrl_col1:
        microclimate = st.selectbox(
            "📍 Select Microclimate Zone:",
            ["Mumbai Coastal (High Humidity)", "Vidarbha Inland (Dry Extreme Heat)", "Urban Heat Island (High Asphalt Density)"],
            index=0
        )
        
    with ctrl_col2:
        preset_choice = st.radio(
            "⚡ 1-Click Historical Weather Presets (Click to Auto-Simulate):",
            ["Custom Sliders", "☀️ Normal Summer (34°C, 50%)", "⚠️ Pre-Monsoon Stress (38.5°C, 65%)", "🔥 2024 Heatwave (41.0°C, 55%)", "🚨 Extreme Emergency (44.0°C, 40%)"],
            horizontal=True
        )

    # Set default values based on preset
    latest_temp = float(df['Max_Temp_C'].iloc[-1])
    latest_rh = float(df['Relative_Humidity_Pct'].iloc[-1])
    
    if preset_choice == "☀️ Normal Summer (34°C, 50%)":
        def_temp, def_rh = 34.0, 50
    elif preset_choice == "⚠️ Pre-Monsoon Stress (38.5°C, 65%)":
        def_temp, def_rh = 38.5, 65
    elif preset_choice == "🔥 2024 Heatwave (41.0°C, 55%)":
        def_temp, def_rh = 41.0, 55
    elif preset_choice == "🚨 Extreme Emergency (44.0°C, 40%)":
        def_temp, def_rh = 44.0, 40
    else:
        def_temp, def_rh = latest_temp, int(latest_rh)

    # 2. Interactive Simulation Sliders
    st.markdown("##### 🎛️ Live Parameter Adjustment")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        sim_temp = st.slider("Simulated Maximum Air Temperature (°C)", 30.0, 48.0, def_temp, 0.5)
    with s_col2:
        sim_rh = st.slider("Simulated Relative Humidity (%)", 15, 95, def_rh, 1)

    # Apply Microclimate Adjustments
    if "Urban Heat Island" in microclimate:
        effective_temp = sim_temp + 1.2  # +1.2C asphalt thermal radiation penalty
    else:
        effective_temp = sim_temp

    # 3. Calculate Apparent Heat Index (NOAA Rothfusz Polynomial)
    tf = effective_temp * 9/5 + 32
    hif = 0.5 * (tf + 61.0 + ((tf - 68.0) * 1.2) + (sim_rh * 0.094))
    if hif >= 80:
        hif = (-42.379 + 2.04901523*tf + 10.14333127*sim_rh - 0.22475541*tf*sim_rh
               - 0.00683783*tf*tf - 0.05481717*sim_rh*sim_rh + 0.00122874*tf*tf*sim_rh
               + 0.00085282*tf*sim_rh*sim_rh - 0.00000199*tf*tf*sim_rh*sim_rh)
    sim_heat_index = round((hif - 32) * 5/9, 1)

    # Calculate Normal Distribution Tail Risk P(T >= 40°C)
    mu_temp = float(df['Max_Temp_C'].mean())
    sigma_temp = float(df['Max_Temp_C'].std())
    z_40 = (40.0 - mu_temp) / sigma_temp
    import math
    prob_exceed_40 = 1.0 - (0.5 * (1.0 + math.erf(z_40 / math.sqrt(2.0))))
    prob_exceed_40_pct = prob_exceed_40 * 100.0

    # Composite Thermal Hazard Score (0 to 100)
    temp_contrib = (effective_temp - 32.0) * 6.5
    rh_contrib = max(0.0, (sim_rh - 35.0) * 0.4)
    raw_hazard_score = temp_contrib + rh_contrib
    hazard_score = int(max(5.0, min(100.0, raw_hazard_score)))

    # 4. Multi-Tier AI Decision Matrix (IMD & NDMA Guidelines)
    if effective_temp >= 42.5 or (effective_temp >= 41.0 and sim_heat_index >= 55.0) or hazard_score >= 80:
        tier_name = "RED ALERT"
        tier_title = "Severe Heatwave Warning (Extreme Emergency Action)"
        card_bg = "#7F1D1D"        # Deep Crimson Red
        border_color = "#EF4444"   # Bright Red Border
        gauge_bar_color = "#DC2626"
        tier_emoji = "🔴"
        rationale = f"Severe thermal disaster threshold breached! Effective temperature ({effective_temp:.1f}°C) and Heat Index ({sim_heat_index:.1f}°C) create acute, life-threatening heatstroke conditions."
        hosp_val = "+180 Beds"
        hosp_desc = "Dedicated Heatstroke ICU Capacity"
        water_val = "+40% Volume"
        water_desc = "Emergency Tanker Fleet Mobilization"
        power_val = "+32% Load"
        power_desc = "Grid AC Surge — Overload Risk"
        directives = [
            "🚨 Immediate red alert broadcast via municipal disaster SMS & radio bulletins.",
            "🏥 Hospital Emergency Protocol: Activate dedicated air-conditioned heatstroke ICU triage centers.",
            "🚧 Labor Directive: Mandatory legal shutdown of all outdoor construction from 11:30 AM to 4:00 PM.",
            "💧 Water Utilities: Pre-position high-capacity water tankers in vulnerable informal settlements.",
            "⚡ Power Grid Management: Ramp up grid spinning reserves to prevent transformer burnout under peak AC cooling loads.",
            "🏫 Educational Institutions: Close all primary schools or restrict hours strictly until 11:00 AM."
        ]
    elif effective_temp >= 40.0 or (effective_temp >= 39.0 and sim_heat_index >= 50.0) or hazard_score >= 60:
        tier_name = "ORANGE ALERT"
        tier_title = "Heatwave Alert (Severe Action Required)"
        card_bg = "#7C2D12"        # Deep Rust Orange
        border_color = "#F97316"   # Bright Orange Border
        gauge_bar_color = "#EA580C"
        tier_emoji = "🟠"
        rationale = f"Official IMD heatwave criteria breached. Sustained thermal accumulation ({effective_temp:.1f}°C) poses severe danger to vulnerable populations."
        hosp_val = "+85 Beds"
        hosp_desc = "Casualty Ward Hydration & Ice Packs"
        water_val = "+25% Volume"
        water_desc = "Transit Kiosks & Pyaaos Active"
        power_val = "+18% Load"
        power_desc = "Substation Peak AC Load Management"
        directives = [
            "⚠️ Issue Orange Alert for high-risk demographics (infants, elderly, chronic illness patients).",
            "🏥 Hospitals: Stock emergency reserves of ORS packets, IV fluids, and ice packs in casualty departments.",
            "🕒 Primary schools adjust afternoon timings; end all outdoor physical activities by 11:00 AM.",
            "💧 Set up public drinking water kiosks ('Pyaaos') at railway stations and transit hubs.",
            "👷 Ensure mandatory shaded rest areas and hydration facilities for municipal street workers."
        ]
    elif effective_temp >= 38.0 or hazard_score >= 40:
        tier_name = "YELLOW ALERT"
        tier_title = "Heat Watch (Advisory & Preparedness)"
        card_bg = "#713F12"        # Deep Golden Bronze
        border_color = "#FACC15"   # Bright Yellow Border
        gauge_bar_color = "#CA8A04"
        tier_emoji = "🟡"
        rationale = f"Elevated temperature ({effective_temp:.1f}°C). Precautionary heat stress advisory active before heatwave thresholds are breached."
        hosp_val = "+30 Beds"
        hosp_desc = "Primary Health Clinic Triage"
        water_val = "+12% Volume"
        water_desc = "Municipal Standby Water Reserves"
        power_val = "+8% Load"
        power_desc = "Precautionary AC Regulation Advisory"
        directives = [
            "🟡 Issue public health warnings on municipal weather portals and local radios.",
            "💧 Check urban drinking water supply lines and ensure park fountains operate.",
            "🩺 Primary health clinics on standby for early dehydration and heat exhaustion cases.",
            "🏢 Advise commercial buildings to regulate AC temperatures to 24°C to conserve energy."
        ]
    else:
        tier_name = "GREEN ALERT"
        tier_title = "Normal Conditions (No Alert)"
        card_bg = "#14532D"        # Deep Forest Green
        border_color = "#22C55E"   # Bright Green Border
        gauge_bar_color = "#16A34A"
        tier_emoji = "🟢"
        rationale = f"Climatic parameters within safe seasonal limits. Temperature ({effective_temp:.1f}°C) poses minimal public health hazard."
        hosp_val = "Baseline (0)"
        hosp_desc = "Standard Hospital Ward Capacity"
        water_val = "Baseline (0%)"
        water_desc = "Standard Municipal Supply Flow"
        power_val = "Baseline (0%)"
        power_desc = "Normal Electrical Grid Operating Load"
        directives = [
            "✅ Standard seasonal meteorological monitoring active.",
            "📊 Routine telemetry logging continues."
        ]

    st.markdown("---")

    # 5. Dual Display: Speedometer Radial Gauge + Solid High-Contrast Banner
    gauge_col, banner_col = st.columns([1, 1.2])

    with gauge_col:
        import plotly.graph_objects as go
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=hazard_score,
            number={
                'font': {'size': 44, 'color': '#FFFFFF', 'family': 'sans-serif'},
                'valueformat': '.0f'
            },
            domain={'x': [0.08, 0.92], 'y': [0.12, 0.88]},
            title={
                'text': "<b>THERMAL HAZARD INDEX</b><br><span style='font-size:0.80em;color:#94A3B8'>Dynamic AI Risk Score (0 to 100)</span>",
                'font': {'size': 15, 'color': '#FFFFFF', 'family': 'sans-serif'}
            },
            gauge={
                'axis': {
                    'range': [0, 100],
                    'tickmode': 'array',
                    'tickvals': [0, 20, 40, 60, 80, 100],
                    'ticktext': ['0', '20', '40', '60', '80', '100'],
                    'tickwidth': 2,
                    'tickcolor': "#94A3B8",
                    'tickfont': {'size': 13, 'color': '#E2E8F0', 'family': 'sans-serif'}
                },
                'bar': {'color': gauge_bar_color, 'thickness': 0.32},
                'bgcolor': "#1E293B",
                'borderwidth': 2,
                'bordercolor': "#475569",
                'steps': [
                    {'range': [0, 40], 'color': '#064E3B'},
                    {'range': [40, 60], 'color': '#713F12'},
                    {'range': [60, 80], 'color': '#7C2D12'},
                    {'range': [80, 100], 'color': '#7F1D1D'}
                ],
                'threshold': {
                    'line': {'color': "#EF4444", 'width': 4},
                    'thickness': 0.75,
                    'value': 80
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor="#0F172A",
            plot_bgcolor="#0F172A",
            height=320,
            margin=dict(l=35, r=35, t=55, b=25)
        )
        st.plotly_chart(fig_gauge, use_container_width=True, theme=None, config={'displayModeBar': False})

    with banner_col:
        alert_html = f"""
        <div style="background-color: {card_bg}; border: 2px solid {border_color}; border-radius: 12px; padding: 1.2rem 1.4rem; box-shadow: 0 4px 15px rgba(0,0,0,0.25); height: 320px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
            <div>
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <span style="font-size: 0.85rem; font-weight: 700; color: #FFFFFF; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.9;">IMD AI Early Warning Protocol</span>
                        <h2 style="margin: 0.2rem 0; color: #FFFFFF !important; font-size: 1.7rem; font-weight: 800;">{tier_emoji} {tier_name}</h2>
                        <div style="color: #F8FAFC; font-weight: 600; font-size: 1.05rem;">{tier_title}</div>
                    </div>
                    <div style="font-size: 2.8rem;">{tier_emoji}</div>
                </div>
                <div style="background: rgba(0, 0, 0, 0.35); border-left: 4px solid #FFFFFF; border-radius: 6px; padding: 0.8rem 1rem; margin-top: 1rem;">
                    <p style="margin: 0; color: #FFFFFF !important; font-size: 0.95rem; line-height: 1.5;">
                        <strong style="color: #FFFFFF;">Statistical Rationale:</strong> {rationale}
                    </p>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 0.6rem; margin-top: 0.6rem;">
                <span style="font-size: 0.82rem; color: #E2E8F0;">Active Zone: <strong>{microclimate.split('(')[0].strip()}</strong></span>
                <span style="font-size: 0.82rem; color: #E2E8F0;">Heat Index: <strong>{sim_heat_index:.1f}°C</strong></span>
            </div>
        </div>
        """
        st.markdown(alert_html, unsafe_allow_html=True)

    st.markdown("---")

    # 6. AI Engineering & Municipal Impact Estimator
    st.subheader("🏥 AI Engineering & Municipal Impact Estimator")
    st.caption("Quantitative resource surge projections calculated from statistical thermal hazard metrics:")

    imp1, imp2, imp3, imp4 = st.columns(4)
    with imp1:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1.1rem; border-left: 5px solid #2563EB; min-height: 125px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.8rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">🌡️ Effective Temp</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #FFFFFF; margin: 0.2rem 0;">{effective_temp:.1f} °C</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">Heat Index: <strong style="color: #60A5FA;">{sim_heat_index:.1f} °C</strong></div>
        </div>
        """, unsafe_allow_html=True)
    with imp2:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1.1rem; border-left: 5px solid #EF4444; min-height: 125px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.8rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">🏥 Hospital Triage</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #FFFFFF; margin: 0.2rem 0;">{hosp_val}</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">{hosp_desc}</div>
        </div>
        """, unsafe_allow_html=True)
    with imp3:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1.1rem; border-left: 5px solid #0284C7; min-height: 125px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.8rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">💧 Water Tankers</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #FFFFFF; margin: 0.2rem 0;">{water_val}</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">{water_desc}</div>
        </div>
        """, unsafe_allow_html=True)
    with imp4:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1.1rem; border-left: 5px solid #F59E0B; min-height: 125px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.8rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">⚡ Power Grid Load</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #FFFFFF; margin: 0.2rem 0;">{power_val}</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">{power_desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 7. Two-Column Analytics: Telemetry vs Thresholds & Municipal Directives
    graph_col, action_col = st.columns([3, 2])

    with graph_col:
        st.subheader("📈 Temperature Telemetry vs IMD Warning Thresholds")
        fig_ts = go.Figure()
        
        # Historical Max Temp line
        fig_ts.add_trace(go.Scatter(
            x=df['Date'], y=df['Max_Temp_C'],
            mode='lines+markers', name='Observed Max Temp',
            line=dict(color='#2563EB', width=2), marker=dict(size=4)
        ))
        
        # Threshold lines
        fig_ts.add_hline(y=40.0, line_dash="dot", line_color="#CA8A04", annotation_text="Heatwatch (40°C)", annotation_position="top left")
        fig_ts.add_hline(y=42.0, line_dash="dot", line_color="#EA580C", annotation_text="Severe Alert (42°C)", annotation_position="top left")
        fig_ts.add_hline(y=44.0, line_dash="dot", line_color="#DC2626", annotation_text="Extreme Emergency (44°C)", annotation_position="top left")
        
        fig_ts.update_layout(
            height=360, margin=dict(l=20, r=20, t=30, b=20),
            xaxis_title="Date", yaxis_title="Temperature (°C)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ts, use_container_width=True)

    with action_col:
        st.subheader("🏛️ Mandated Engineering & Municipal Directives")
        for directive in directives:
            st.markdown(f"- {directive}")

    st.markdown("---")

    # 8. One-Click Official Municipal Action Plan Bulletin Download
    st.subheader("📥 Official Municipal Early Warning Bulletin")
    st.caption("Generate and download the official disaster management action bulletin for this simulated scenario:")

    official_bulletin = f"""================================================================================
MUNICIPAL CORPORATION DISASTER MANAGEMENT CELL
HEATWAVE EARLY WARNING ACTION PLAN BULLETIN
Issued under IMD & NDMA National Guidelines | STAT-AI IA1
================================================================================
Timestamp: Current Assessment Simulation
Microclimate Zone: {microclimate}
Alert Level: {tier_emoji} {tier_name} ({tier_title})
Composite Thermal Hazard Index: {hazard_score} / 100

METEOROLOGICAL PARAMETERS:
- Simulated Surface Temperature: {effective_temp:.1f} °C
- Relative Humidity: {sim_rh} %
- Apparent Heat Index (NOAA): {sim_heat_index:.1f} °C
- Seasonal Baseline Mean (μ): {mu_temp:.2f} °C
- Baseline P(T >= 40°C): {prob_exceed_40_pct:.2f} %

PROJECTED MUNICIPAL IMPACT:
- Hospital Emergency Heatstroke Load: {hosp_val} ({hosp_desc})
- Municipal Water Supply Surge: {water_val} ({water_desc})
- Power Grid Cooling Load Surge: {power_val} ({power_desc})

MANDATED CIVIL DIRECTIVES:
{chr(10).join(['* ' + d for d in directives])}

STATISTICAL RATIONALE:
{rationale}
================================================================================
"""
    st.download_button(
        label="📄 Download Official Heatwave Advisory Bulletin (.txt)",
        data=official_bulletin,
        file_name=f"IMD_Heatwave_Advisory_{tier_name.replace(' ', '_')}.txt",
        mime="text/plain"
    )



