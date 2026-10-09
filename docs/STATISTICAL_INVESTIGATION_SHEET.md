# STATISTICAL INVESTIGATION SHEET
## Academic Year 2026–27 | S.Y. B.Tech Engineering
### Course: Statistical Methods and Probability (SMP) | Internal Assessment – IA 1
**Theme:** STAT-AI Engineering Challenge — *From Data to Decision*  
**Case Study 1:** AI-Based Heatwave Monitoring and Early Warning System  
**Submission Format:** `GroupNumber_TopicName_StatAI_IA1`  
**Evaluation Marks:** 20 Marks (Mode: Interactive Demonstration & Viva)

---

## 1. Problem Statement
Heatwaves represent one of the most hazardous meteorological extremes in India, leading to heat strokes, agricultural stress, municipal water strain, and electrical power grid surges. Conventional monitoring often relies on retrospective or isolated daily alerts.  
The engineering objective is to design an **AI-Supported Statistical Early Warning System** that continuously ingests daily temperature and humidity telemetry, performs rigorous descriptive and inferential statistical modeling, and automatically transitions between municipal action levels (**Green, Yellow, Orange, Red**) to enable pre-emptive disaster mitigation.

---

## 2. Description of the Dataset
- **Source of Data:** India Meteorological Department (IMD) / Open Government Data Platform India (`data.gov.in`) & NASA POWER Meteorological API.
- **Geographic Focus:** Mumbai & Vidarbha Region, Maharashtra, India.
- **Observation Count ($N$):** 65 daily sequential observations covering the pre-monsoon summer spell (March 15 to May 18, 2026).
- **Recorded Variables:**
  1. `Date`: Chronological date sequence (`YYYY-MM-DD`).
  2. `Max_Temp_C`: Daily maximum surface air temperature ($^\circ\text{C}$).
  3. `Min_Temp_C`: Daily minimum surface air temperature ($^\circ\text{C}$).
  4. `Relative_Humidity_Pct`: Afternoon relative humidity ($\%$).
  5. `Heat_Index_C`: NOAA Apparent Temperature calculated via the Rothfusz polynomial ($^\circ\text{C}$).
  6. `Weather_Condition`: Categorical classification (`Normal`, `Moderate Heat`, `Heatwave`, `Severe Heatwave`).

---

## 3. Statistical Concepts Used & Relevant Formulae

### A. Data Hygiene & Outlier Detection (IQR Method)
- First Quartile ($Q_1$): $25^{\text{th}}$ percentile; Third Quartile ($Q_3$): $75^{\text{th}}$ percentile.
- Interquartile Range:
  $$\text{IQR} = Q_3 - Q_1$$
- Inner Fences:
  $$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}, \quad \text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$

### B. Measures of Central Tendency & Dispersion
- **Sample Mean ($\bar{x}$):**
  $$\bar{x} = \frac{\sum_{i=1}^N x_i}{N}$$
- **Sample Variance ($s^2$) & Standard Deviation ($s$):**
  $$s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}, \quad s = \sqrt{s^2}$$
- **Coefficient of Variation ($CV$):**
  $$CV = \left( \frac{s}{\bar{x}} \right) \times 100\%$$
- **Grouped Mean:**
  $$\bar{x}_{\text{grouped}} = \frac{\sum f_i x_i}{\sum f_i}$$

### C. Extreme Temperature Modeling (Gaussian / Normal Distribution)
Assuming $X \sim \mathcal{N}(\mu, \sigma^2)$:
- **Standard Normal Variable ($Z$):**
  $$Z = \frac{X - \mu}{\sigma}$$
- **Tail Exceedance Probability ($P(X \ge T)$):**
  $$P(X \ge T) = 1 - \Phi(Z) = \int_{T}^\infty \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left( \frac{x-\mu}{\sigma} \right)^2} dx$$

### D. Joint & Conditional Probability and Bayesian Inference
- **Conditional Probability:**
  $$P(\text{Heatwave} \mid \text{High Humidity}) = \frac{n(\text{Heatwave} \cap \text{High Humidity})}{n(\text{High Humidity})}$$
- **Bayes' Theorem for IoT Weather Sensor Alarm:**
  $$P(H \mid S) = \frac{P(S \mid H) \cdot P(H)}{P(S \mid H) \cdot P(H) + P(S \mid \neg H) \cdot P(\neg H)}$$
  Where $H$ is true heatwave state and $S$ is sensor alarm trigger.

### E. Discrete Random Process & Autocorrelation
- **Sample Autocorrelation Function (ACF):**
  $$r_k = \frac{\sum_{t=1}^{N-k} (X_t - \bar{x})(X_{t+k} - \bar{x})}{\sum_{t=1}^N (X_t - \bar{x})^2}, \quad k \in \{1, 2, \dots, 7\}$$
- **95% Confidence Bounds:**
  $$\text{CI}_{95\%} = \pm \frac{1.96}{\sqrt{N}}$$

---

## 4. Step-by-Step Numerical Calculations

### Calculation 1: Descriptive Statistics
For $N = 65$ observations of Maximum Temperature ($T_{\max}$):
- $\sum_{i=1}^{65} x_i = 2505.40^\circ\text{C}$
- Mean:
  $$\bar{x} = \frac{2505.40}{65} = 38.54^\circ\text{C}$$
- Median: $M_d = 38.40^\circ\text{C}$
- $\sum (x_i - \bar{x})^2 = 636.88$
- Variance:
  $$s^2 = \frac{636.88}{65 - 1} = \frac{636.88}{64} = 9.9512\ (^\circ\text{C})^2$$
- Standard Deviation:
  $$s = \sqrt{9.9512} = 3.15^\circ\text{C}$$
- Coefficient of Variation:
  $$CV = \left( \frac{3.15}{38.54} \right) \times 100\% = 8.18\%$$

### Calculation 2: Continuous Frequency Distribution
| Class Interval ($^\circ\text{C}$) | Class Mark ($x_i$) | Frequency ($f_i$) | Cumulative Freq ($cf$) | Relative Freq ($\%$) | $f_i x_i$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 32.0 – 34.0 | 33.00 | 5 | 5 | 7.69% | 165.00 |
| 34.0 – 36.0 | 35.00 | 11 | 16 | 16.92% | 385.00 |
| 36.0 – 38.0 | 37.00 | 16 | 32 | 24.62% | 592.00 |
| 38.0 – 40.0 | 39.00 | 14 | 46 | 21.54% | 546.00 |
| 40.0 – 42.0 | 41.00 | 12 | 58 | 18.46% | 492.00 |
| 42.0 – 44.0 | 43.00 | 5 | 63 | 7.69% | 215.00 |
| 44.0 – 46.0 | 45.00 | 2 | 65 | 3.08% | 90.00 |
| **Total** | — | **$N = 65$** | — | **100.00%** | **2485.00** |

- Grouped Mean:
  $$\bar{x}_{\text{grouped}} = \frac{2485.00}{65} = 38.23^\circ\text{C}$$

### Calculation 3: Extreme Value Probability via Normal Distribution
Fitting $\mathcal{N}(\mu = 38.54^\circ\text{C}, \sigma = 3.15^\circ\text{C})$:
- **Threshold $T = 40.0^\circ\text{C}$ (Heatwave Alert):**
  $$Z_{40} = \frac{40.0 - 38.54}{3.15} = +0.4635$$
  $$P(X \ge 40.0^\circ\text{C}) = 1 - \Phi(0.4635) = 1 - 0.6785 = 0.3215\ (32.15\%)$$
- **Threshold $T = 42.0^\circ\text{C}$ (Severe Heatwave):**
  $$Z_{42} = \frac{42.0 - 38.54}{3.15} = +1.0984$$
  $$P(X \ge 42.0^\circ\text{C}) = 1 - \Phi(1.0984) = 1 - 0.8640 = 0.1360\ (13.60\%)$$
- **Threshold $T = 45.0^\circ\text{C}$ (Extreme Catastrophe):**
  $$Z_{45} = \frac{45.0 - 38.54}{3.15} = +2.0508$$
  $$P(X \ge 45.0^\circ\text{C}) = 1 - \Phi(2.0508) = 1 - 0.9798 = 0.0202\ (2.02\%)$$

### Calculation 4: Bayesian Sensor Update
- Historical Prior Heatwave Probability: $P(H) = 19/65 = 0.2923\ (29.23\%)$
- Sensor True Positive Rate: $P(S \mid H) = 0.92$
- Sensor False Alarm Rate: $P(S \mid \neg H) = 0.08$
- Marginal Sensor Alert Probability:
  $$P(S) = (0.92 \times 0.2923) + (0.08 \times 0.7077) = 0.2689 + 0.0566 = 0.3255$$
- Posterior Probability:
  $$P(H \mid S) = \frac{0.2689}{0.3255} = 0.8261\ (82.61\%)$$

### Calculation 5: Autocorrelation & Random Process
- Number of observations $N = 65 \implies \text{CI}_{95\%} = \pm \frac{1.96}{\sqrt{65}} = \pm 0.2431$
- Lag-1 Autocorrelation:
  $$r_1 = 0.7682 \quad (\gg +0.2431 \implies \text{Statistically Significant})$$
- Lag-2 Autocorrelation: $r_2 = 0.5420$
- **Inference:** Thermal memory persists for 2–3 consecutive days. Heatwaves do not behave as memoryless white noise; they form autocorrelated multi-day spells.

---

## 5. AI / Engineering Decision Matrix
Based on synthesized statistical inputs, the system triggers official disaster responses:

| Alert Level | Trigger Condition | Statistical Indicator | Mandated Engineering / Civil Action |
| :---: | :---: | :---: | :--- |
| **GREEN** | $T < 38^\circ\text{C}$ | $P(T \ge 40) < 15\%$ | Routine meteorological logging; normal municipal operations. |
| **YELLOW** | $38^\circ\text{C} \le T < 40^\circ\text{C}$ | $P(T \ge 40) \in [15\%, 35\%)$ | Public health warnings; pre-position water tankers; hospital hydration stations. |
| **ORANGE** | $40^\circ\text{C} \le T < 42^\circ\text{C}$ OR Streak $\ge 2$ days | $P(T \ge 40) \ge 40\%$ OR $P(H \mid S) > 80\%$ | Primary school afternoon closures; halt outdoor construction 12:00–3:30 PM; standby ORS beds. |
| **RED** | $T \ge 42^\circ\text{C}$ OR Heat Index $\ge 50^\circ\text{C}$ | $P(T \ge 42) \ge 35\%$ | Emergency heatstroke ICU activation; grid spinning reserve ramp-up; municipal emergency broadcasts. |

---

## 6. Limitations of the Statistical Model
1. **Gaussian Distribution Assumption:** While temperatures generally follow a bell shape, extreme heat events possess asymmetric right-tail skewness (extreme value Frechet/Gumbel distribution provides higher tail fidelity).
2. **Stationarity Bounds:** Meteorological processes are non-stationary across season transitions (e.g., transition from pre-monsoon dry heat to monsoonal humidity).
3. **Microclimate Variations:** Urban Heat Island (UHI) effects cause localized asphalt temperature variances not captured by a single regional meteorological station.

---

## 7. References
1. India Meteorological Department (IMD), *Criteria for Declaring Heat Wave and Severe Heat Wave in India*, Government of India.
2. National Disaster Management Authority (NDMA), *National Guidelines for Preparation of Action Plan - Prevention and Management of Heat Wave*.
3. National Oceanic and Atmospheric Administration (NOAA), *The Heat Index Equation and Rothfusz Regression*, National Weather Service.
