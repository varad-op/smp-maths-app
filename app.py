import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from modules.time_series_process import compute_autocorrelation, analyze_stationarity, detect_heatwave_streaks

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
    "📊 Tab 1: Data Ingestion & Frequency",
    "📐 Tab 2: Member 2 (Descriptive Stats)",
    "🔔 Tab 3: Normal Distribution",
    "🎲 Tab 4: Member 4 (Bayesian Inference)",
    "⏳ Tab 5: Random Process & Time-Series",
    "🚨 Tab 6: AI Decision Engine"
])

# ==============================================================================
# TAB 1: DATA INGESTION & FREQUENCY DISTRIBUTION
# ==============================================================================
with tab1:
    st.header("📊 Data Ingestion & Frequency Distribution")
    
    st.markdown("### 🟢 Meteorological Telemetry Overview & Exploratory Analysis")
    
    # 1. Metric cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Observations (N)", value=len(df))
    with col2:
        st.metric(label="Minimum Temp Recorded", value=f"{df['Max_Temp_C'].min():.1f} °C")
    with col3:
        st.metric(label="Maximum Temp Recorded", value=f"{df['Max_Temp_C'].max():.1f} °C")
        
    st.markdown("---")
    
    # 2. Interquartile Range (IQR) & Outlier Screening
    st.subheader("Interquartile Range (IQR) & Outlier Screening")
    q1 = df['Max_Temp_C'].quantile(0.25)
    q3 = df['Max_Temp_C'].quantile(0.75)
    iqr = q3 - q1
    
    # Display formula using st.latex
    st.latex(r"IQR = Q_3 - Q_1")
    st.latex(rf"IQR = {q3:.2f}^\circ\text{{C}} - {q1:.2f}^\circ\text{{C}} = {iqr:.2f}^\circ\text{{C}}")
    
    st.markdown("---")
    
    # 3. Interactive Temperature Histogram
    st.subheader("Temperature Distribution Histogram")
    fig = px.histogram(
        df, 
        x="Max_Temp_C", 
        nbins=7, 
        title="Frequency Distribution of Maximum Temperatures",
        labels={"Max_Temp_C": "Max Temperature (°C)"},
        color_discrete_sequence=['#3B82F6']
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

    # 4. Continuous Frequency Distribution Table (7 Bins)
    st.subheader("📋 Continuous Frequency Distribution Table (7 Bins)")

    # Select temperature data and remove missing values
    temp_data = df["Max_Temp_C"].dropna()

    # Calculate range and class width
    min_temp = temp_data.min()
    max_temp = temp_data.max()
    data_range = max_temp - min_temp
    class_width = data_range / 7

    st.markdown("### Step 1: Calculate Range and Class Width")

    st.latex(r"\text{Range} = X_{\max} - X_{\min}")
    st.latex(
        rf"\text{{Range}} = {max_temp:.2f} - {min_temp:.2f}"
        rf" = {data_range:.2f}"
    )

    st.latex(r"\text{Class Width} = \frac{\text{Range}}{7}")
    st.latex(
        rf"\text{{Class Width}} = \frac{{{data_range:.2f}}}{{7}}"
        rf" = {class_width:.2f}"
    )

    # Create 7 equal-width continuous class intervals
    bin_edges = np.linspace(min_temp, max_temp, 8)

    frequencies, edges = np.histogram(
        temp_data,
        bins=bin_edges
    )

    cumulative_frequency = np.cumsum(frequencies)

    frequency_table = pd.DataFrame({
        "Class Interval (°C)": [
            f"{edges[i]:.2f} – {edges[i + 1]:.2f}"
            for i in range(7)
        ],
        "Lower Boundary (°C)": edges[:-1].round(2),
        "Upper Boundary (°C)": edges[1:].round(2),
        "Frequency (f)": frequencies,
        "Cumulative Frequency (cf)": cumulative_frequency
    })

    st.dataframe(frequency_table, use_container_width=True)

    st.metric(
        label="Total Observations",
        value=int(frequencies.sum())
    )

    st.markdown("---")

    # 5. Ogive Curve
    st.subheader("📈 Less-Than Ogive Curve")

    st.write(
        "An ogive is a graph of cumulative frequency "
        "plotted against the upper class boundaries."
    )

    ogive_df = pd.DataFrame({
        "Upper Class Boundary (°C)": edges[1:],
        "Cumulative Frequency": cumulative_frequency
    })

    # Add the starting point of the ogive
    start_point = pd.DataFrame({
        "Upper Class Boundary (°C)": [edges[0]],
        "Cumulative Frequency": [0]
    })

    ogive_df = pd.concat(
        [start_point, ogive_df],
        ignore_index=True
    )

    fig_ogive = px.line(
        ogive_df,
        x="Upper Class Boundary (°C)",
        y="Cumulative Frequency",
        markers=True,
        title="Less-Than Ogive: Mumbai–Maharashtra Maximum Temperatures",
        labels={
            "Upper Class Boundary (°C)": "Upper Class Boundary (°C)",
            "Cumulative Frequency": "Cumulative Frequency"
        },
        text="Cumulative Frequency"
    )

    fig_ogive.update_traces(line=dict(width=3))

    fig_ogive.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

    st.plotly_chart(fig_ogive, use_container_width=True)

    st.success(
        "Frequency table and less-than ogive generated successfully!"
    )


# ==============================================================================
# TAB 2: MEMBER 2 (DESCRIPTIVE STATISTICS & DISPERSION)
# ==============================================================================
with tab2:
   
    st.header("📐Descriptive Statistics & Measures of Dispersion")
    
    st.markdown("""
    This section summarizes the daily maximum temperature data using measures of
    central tendency and dispersion. Missing or non-numeric temperature values are
    ignored in the calculations.
    """)
    st.markdown("---")

    st.subheader("1. Clean Temperature Data")
    temp = pd.to_numeric(df["Max_Temp_C"], errors="coerce").dropna()
    n = len(temp)

    if n == 0:
        st.warning("No valid maximum-temperature values were found in the dataset.")
    else:
        sample_mean = float(temp.mean())
        median_val = float(temp.median())
        modes = temp.mode().tolist()
        min_temp = float(temp.min())
        max_temp = float(temp.max())
        range_val = max_temp - min_temp
        variance_val = float(temp.var(ddof=1)) if n > 1 else float("nan")
        sample_std = float(temp.std(ddof=1)) if n > 1 else float("nan")
        cv_val = (sample_std / abs(sample_mean) * 100) if n > 1 and sample_mean != 0 else float("nan")
        sum_x = float(temp.sum())
        sum_sq_diff = float(((temp - sample_mean) ** 2).sum())

        st.caption(f"Valid observations used: {n}")
        st.markdown("---")

        st.subheader("2. Measures of Central Tendency")
        c1, c2, c3 = st.columns(3)
        c1.metric("Mean", f"{sample_mean:.2f} °C")
        c2.metric("Median", f"{median_val:.2f} °C")
        c3.metric("Number of observations (n)", f"{n}")

        st.markdown("**Mean formula**")
        st.latex(r"\bar{x} = \frac{\sum x_i}{n}")
        st.latex(rf"\bar{{x}} = \frac{{{sum_x:.2f}}}{{{n}}} = {sample_mean:.2f}^\circ C")

        st.markdown("**Median**")
        st.write(f"The median is the middle value after sorting the {n} valid temperature observations: **{median_val:.2f} °C**.")

        st.markdown("**Mode**")
        if len(modes) == 1:
            st.write(f"Most frequent temperature: **{modes[0]:.2f} °C**.")
        else:
            mode_text = ", ".join(f"{value:.2f} °C" for value in modes)
            st.write(f"The data are multimodal. Most frequent values: **{mode_text}**.")

        st.markdown("---")
        st.subheader("3. Measures of Dispersion")
        d1, d2, d3 = st.columns(3)
        d1.metric("Minimum", f"{min_temp:.2f} °C")
        d2.metric("Maximum", f"{max_temp:.2f} °C")
        d3.metric("Range", f"{range_val:.2f} °C")

        d4, d5, d6 = st.columns(3)
        d4.metric("Sample Variance", f"{variance_val:.4f} °C²" if n > 1 else "Not available")
        d5.metric("Sample Standard Deviation", f"{sample_std:.2f} °C" if n > 1 else "Not available")
        d6.metric("Coefficient of Variation", f"{cv_val:.2f} %" if n > 1 and sample_mean != 0 else "Not available")

        st.markdown("**Range formula**")
        st.latex(r"\text{Range} = x_{\max} - x_{\min}")
        st.latex(rf"\text{{Range}} = {max_temp:.2f} - {min_temp:.2f} = {range_val:.2f}^\circ C")

        if n > 1:
            st.markdown("**Sample variance formula**")
            st.latex(r"s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}")
            st.latex(rf"s^2 = \frac{{{sum_sq_diff:.4f}}}{{{n}-1}} = {variance_val:.4f}\ ^\circ C^2")

            st.markdown("**Sample standard deviation formula**")
            st.latex(r"s = \sqrt{s^2}")
            st.latex(rf"s = \sqrt{{{variance_val:.4f}}} = {sample_std:.2f}^\circ C")

            st.markdown("**Coefficient of variation formula**")
            st.latex(r"CV = \frac{s}{|\bar{x}|} \times 100\%")
            if sample_mean != 0:
                st.latex(rf"CV = \frac{{{sample_std:.2f}}}{{|{sample_mean:.2f}|}} \times 100\% = {cv_val:.2f}\%")

        st.markdown("---")
        st.subheader("4. Box-and-Whisker Plot")
        plot_df = pd.DataFrame({"Max_Temp_C": temp})
        fig_box = px.box(
            plot_df,
            y="Max_Temp_C",
            points="all",
            title="Distribution of Daily Maximum Temperatures",
            labels={"Max_Temp_C": "Maximum Temperature (°C)"}
        )
        fig_box.update_layout(template="plotly_white", yaxis_title="Maximum Temperature (°C)")
        st.plotly_chart(fig_box, use_container_width=True)

        st.subheader("5. Brief Interpretation")
        st.write(f"- The average daily maximum temperature is **{sample_mean:.2f} °C**.")
        st.write(f"- The observed temperatures span **{range_val:.2f} °C**, from {min_temp:.2f} °C to {max_temp:.2f} °C.")
        if n > 1:
            st.write(f"- The sample standard deviation is **{sample_std:.2f} °C**, describing the typical spread around the mean.")
            st.write(f"- The coefficient of variation is **{cv_val:.2f}%**, which expresses standard deviation relative to the mean.")




# ==============================================================================
# TAB 3: NORMAL DISTRIBUTION & EXTREME VALUES
# ==============================================================================
with tab3:
    import math
    import plotly.graph_objects as go

    st.header("🔔 Normal Distribution & Extreme Values")

    mu = df['Max_Temp_C'].mean()
    sigma = df['Max_Temp_C'].std()

    st.write(f"Mean: {mu:.2f}°C")
    st.write(f"Standard deviation: {sigma:.2f}°C")
    st.latex(rf"T \sim N({mu:.2f}, {sigma**2:.2f})")

    t = st.slider("Temperature threshold (°C)", 36.0, 48.0, 40.0, 0.5)
    z = (t - mu) / sigma
    p = 0.5 * math.erfc(z / math.sqrt(2))

    st.latex(rf"Z = \frac{{{t}-{mu:.2f}}}{{{sigma:.2f}}} = {z:.4f}")
    st.latex(r"P(T \ge t) = 1-\Phi(Z)")
    st.metric(f"Probability of temperature ≥ {t}°C", f"{p*100:.2f}%")

    for temperature in [40, 42, 45]:
        z_value = (temperature - mu) / sigma
        probability = 0.5 * math.erfc(z_value / math.sqrt(2))
        st.write(f"{temperature}°C: Z = {z_value:.4f}, Probability = {probability*100:.2f}%")

    x = np.linspace(min(mu-5*sigma, t-sigma), max(mu+5*sigma, t+sigma), 500)
    x = np.sort(np.append(x, t))
    y = np.exp(-0.5*((x-mu)/sigma)**2) / (sigma*math.sqrt(2*math.pi))

    fig = go.Figure(go.Scatter(x=x, y=y, mode="lines", name="Bell curve"))
    fig.add_trace(go.Scatter(
        x=x[x >= t], y=y[x >= t],
        mode="lines", fill="tozeroy", name="Probability area"
    ))
    fig.add_vline(x=t, line_dash="dash")
    fig.update_layout(xaxis_title="Temperature (°C)", yaxis_title="Probability density")
    st.plotly_chart(fig, use_container_width=True)

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
# TAB 5: TIME SERIES & RANDOM PROCESS
# ==============================================================================
with tab5:
    st.header("⏳ Temperature as a Random Process & Autocorrelation")

    st.markdown("---")
    st.subheader("💻 Time-Series Analysis")

    # Prepare a clean, chronological copy for Member 5 only.
    ts_df = df[["Date", "Max_Temp_C"]].copy()
    ts_df["Date"] = pd.to_datetime(ts_df["Date"], errors="coerce")
    ts_df["Max_Temp_C"] = pd.to_numeric(ts_df["Max_Temp_C"], errors="coerce")
    ts_df = (
        ts_df.dropna(subset=["Date", "Max_Temp_C"])
        .sort_values("Date")
        .reset_index(drop=True)
    )

    if len(ts_df) < 8:
        st.warning("At least 8 valid daily temperature observations are needed to calculate ACF for lags 1–7.")
    else:
        # Calculate autocorrelation values for lags 1 through 7 and the 95% bounds.
        acf_df, ci_bound, formula_steps = compute_autocorrelation(
            ts_df["Max_Temp_C"], max_lags=7
        )
        lag1_autocorr = float(
            acf_df.loc[acf_df["Lag (Days)"] == 1, "Autocorrelation (rk)"].iloc[0]
        )

        # Enhanced metric cards: clearer labels, interpretations, and visual grouping.
        col1, col2 = st.columns(2, gap="medium")

        with col1:
            with st.container(border=True):
                st.markdown("### 🔗 Autocorrelation")
                st.metric(
                    label="Lag-1 Autocorrelation (r₁)",
                    value=f"{lag1_autocorr:.4f}",
                    delta=(
                        "Strong positive relationship"
                        if lag1_autocorr > 0.5
                        else "Weak or moderate relationship"
                    ),
                    delta_color="off",
                )
                st.caption(
                    "How strongly today's temperature is related "
                    "to the previous day's temperature."
                )

        with col2:
            with st.container(border=True):
                st.markdown("### 📊 Confidence Interval")
                st.metric(
                    label="95% Bartlett Confidence Bound",
                    value=f"± {ci_bound:.4f}",
                    delta=f"Range: −{ci_bound:.4f} to +{ci_bound:.4f}",
                    delta_color="off",
                )
                st.caption(
                    "Autocorrelation values outside these bounds are "
                    "approximately significant at the 5% level."
                )

        if abs(lag1_autocorr) > ci_bound:
            st.success(
                f"📈 Lag-1 autocorrelation ({lag1_autocorr:.4f}) lies outside "
                "the confidence bounds, indicating statistically significant "
                "autocorrelation under this approximate test."
            )
        else:
            st.info(
                "Lag-1 autocorrelation lies within the confidence bounds."
            )

        st.subheader("1. Correlogram (Autocorrelation Function)")
        st.write(
            "Each bar shows the autocorrelation between daily maximum temperature and "
            "temperature a given number of days later. Bars outside the dashed confidence "
            "bounds are flagged as statistically significant by this approximate rule."
        )
        acf_fig = px.bar(
            acf_df,
            x="Lag (Days)",
            y="Autocorrelation (rk)",
            title="Autocorrelation of Daily Maximum Temperature (Lags 1–7)",
            labels={
                "Lag (Days)": "Lag (days)",
                "Autocorrelation (rk)": "Autocorrelation coefficient",
            },
            hover_data={"Statistically Significant": True},
        )
        acf_fig.add_hline(
            y=ci_bound,
            line_dash="dash",
            line_color="red",
            annotation_text=f"+95% bound ({ci_bound:.3f})",
        )
        acf_fig.add_hline(
            y=-ci_bound,
            line_dash="dash",
            line_color="red",
            annotation_text=f"−95% bound (−{ci_bound:.3f})",
        )
        acf_fig.add_hline(y=0, line_color="gray", line_width=1)
        acf_fig.update_layout(xaxis=dict(dtick=1))
        st.plotly_chart(acf_fig, use_container_width=True)
        st.dataframe(acf_df, use_container_width=True, hide_index=True)

        st.subheader("2. Daily Temperature and 7-Day Rolling Mean")
        stationarity = analyze_stationarity(ts_df, window=7)
        rolling_df = pd.DataFrame(
            {
                "Date": ts_df["Date"],
                "Daily Maximum Temperature (°C)": ts_df["Max_Temp_C"],
                "7-Day Rolling Mean (°C)": stationarity["rolling_mean"],
            }
        )
        mean_fig = px.line(
            rolling_df,
            x="Date",
            y=["Daily Maximum Temperature (°C)", "7-Day Rolling Mean (°C)"],
            title="Daily Maximum Temperature with 7-Day Rolling Mean",
            labels={"value": "Temperature (°C)", "Date": "Date", "variable": "Series"},
        )
        mean_fig.update_traces(connectgaps=False)
        st.plotly_chart(mean_fig, use_container_width=True)
        st.caption(
            f"Rolling-mean range: {stationarity['mean_diff']} °C. "
            f"Rolling standard-deviation range: {stationarity['std_diff']} °C. "
            "Rolling summaries help inspect possible changes over time; they do not alone prove stationarity."
        )

        st.subheader("3. Heatwave Streaks (Temperature ≥ 40°C)")
        st.caption(
            "This uses the project's 40°C threshold to identify runs of at least two consecutive observations. "
            "It is a project rule and not necessarily the official IMD heatwave definition."
        )
        streak_df = detect_heatwave_streaks(ts_df, threshold=40.0)
        hot_day_count = int((ts_df["Max_Temp_C"] >= 40.0).sum())
        st.metric("Days with maximum temperature ≥ 40°C", hot_day_count)
        if streak_df.empty:
            st.info("No streak of two or more consecutive days at or above 40°C was found in this dataset.")
        else:
            st.dataframe(streak_df, use_container_width=True, hide_index=True)
            longest = streak_df.loc[streak_df["Duration (Days)"].idxmax()]
            st.write(
                f"**Longest detected streak:** {int(longest['Duration (Days)'])} days, "
                f"starting {longest['Start Date']}; peak temperature "
                f"{longest['Peak Temp (°C)']:.1f} °C."
            )



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
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1rem 1.1rem; border-left: 5px solid #2563EB; height: 150px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.78rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">🌡️ Effective Temp</div>
            <div style="font-size: 1.55rem; font-weight: 800; color: #FFFFFF; margin: 0.15rem 0; white-space: nowrap;">{effective_temp:.1f} °C</div>
            <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.35; min-height: 2.4rem; display: flex; align-items: flex-start;">Heat Index: <strong style="color: #60A5FA; margin-left: 4px;">{sim_heat_index:.1f} °C</strong></div>
        </div>
        """, unsafe_allow_html=True)
    with imp2:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1rem 1.1rem; border-left: 5px solid #EF4444; height: 150px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.78rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">🏥 Hospital Triage</div>
            <div style="font-size: 1.55rem; font-weight: 800; color: #FFFFFF; margin: 0.15rem 0; white-space: nowrap;">{hosp_val}</div>
            <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.35; min-height: 2.4rem; display: flex; align-items: flex-start;">{hosp_desc}</div>
        </div>
        """, unsafe_allow_html=True)
    with imp3:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1rem 1.1rem; border-left: 5px solid #0284C7; height: 150px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.78rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">💧 Water Tankers</div>
            <div style="font-size: 1.55rem; font-weight: 800; color: #FFFFFF; margin: 0.15rem 0; white-space: nowrap;">{water_val}</div>
            <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.35; min-height: 2.4rem; display: flex; align-items: flex-start;">{water_desc}</div>
        </div>
        """, unsafe_allow_html=True)
    with imp4:
        st.markdown(f"""
        <div style="background: #0F172A; border: 1px solid #334155; border-radius: 10px; padding: 1rem 1.1rem; border-left: 5px solid #F59E0B; height: 150px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            <div style="font-size: 0.78rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">⚡ Power Grid Load</div>
            <div style="font-size: 1.55rem; font-weight: 800; color: #FFFFFF; margin: 0.15rem 0; white-space: nowrap;">{power_val}</div>
            <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.35; min-height: 2.4rem; display: flex; align-items: flex-start;">{power_desc}</div>
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



