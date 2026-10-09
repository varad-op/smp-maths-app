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
    "🚨 Tab 6: Member 6 (AI Decision Engine)"
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
# TAB 6: MEMBER 6 (AI DECISION ENGINE & EARLY WARNING SYSTEM)
# ==============================================================================
with tab6:
    st.header("🚨 Member 6: AI Decision Engine & Early Warning System")
    st.write("**Assigned Role:** AI Decision Engine & UI Lead (Team Lead) | **Presentation Slot:** Min 5:30 – 6:45")
    
    st.markdown(r"""
    #### 📝 What Member 6 needs to put here:
    1. **Rule-Based AI Early Warning Matrix:** Map probabilities and temperatures to official IMD alert tiers:
       - 🟢 **GREEN (Normal):** $T < 38^\circ\text{C}$
       - 🟡 **YELLOW (Heat Watch):** $38^\circ\text{C} \le T < 40^\circ\text{C}$
       - 🟠 **ORANGE (Heat Alert):** $40^\circ\text{C} \le T < 42^\circ\text{C}$
       - 🔴 **RED (Severe Warning):** $T \ge 42^\circ\text{C}$ or Extreme Heat Index
    2. **Municipal Action Directives:** Action list for hospitals, schools, outdoor workers, and water supplies.
    3. **Live Demonstration:** Let the evaluator test a simulated temperature offset to see the alert trigger change!
    """)
    
    st.markdown("---")
    st.subheader("💻 Member 6 Starter Code Area:")
    
    # --- TODO: MEMBER 6 WRITE YOUR AI DECISION ENGINE HERE ---
    current_temp = float(df['Max_Temp_C'].iloc[-1])
    
    # Example alert logic
    if current_temp >= 42.0:
        st.error(f"🔴 RED ALERT ({current_temp:.1f}°C): Activate Hospital Heatstroke Emergency Protocol!")
    elif current_temp >= 40.0:
        st.warning(f"🟠 ORANGE ALERT ({current_temp:.1f}°C): Enforce afternoon outdoor construction ban (12-4 PM).")
    elif current_temp >= 38.0:
        st.info(f"🟡 YELLOW ALERT ({current_temp:.1f}°C): Issue public hydration and heat watch advisory.")
    else:
        st.success(f"🟢 GREEN ALERT ({current_temp:.1f}°C): Normal seasonal conditions.")

