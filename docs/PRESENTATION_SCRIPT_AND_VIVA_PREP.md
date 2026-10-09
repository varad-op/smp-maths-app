# 🎤 6-7 MINUTE SHOWCASE SCRIPT & VIVA PREPARATION GUIDE
## Course: Statistical Methods and Probability (IA-1) | Somaiya Vidyavihar University
### Case Study 1: AI-Based Heatwave Monitoring and Early Warning System

> [!IMPORTANT]
> **NO PPT IS PERMITTED!** You will present directly from the **Live Streamlit Web Application**.
> Total Presentation Duration: **6 to 7 minutes strictly**.  
> Every member speaks for ~1 minute. Follow the exact cues and live clicks below!

---

## ⏱️ Word-for-Word Showcase Script (6–7 Minutes)

### Member 1: Data Engineering & Ingestion Lead (Min 0:00 – 1:00)
- **Action on Screen:** Open Web App -> Click on **Tab 2: "1. Data & Frequency (M1)"**.
- **Script:**
  > *"Good morning respected Professor and evaluators. Our project tackles **Case Study 1: AI-Based Heatwave Monitoring and Early Warning System** under the STAT-AI Engineering theme — 'From Data to Decision'.  
  > I am Member 1, responsible for Data Engineering and Ingestion. We ingested 65 daily observations from the India Meteorological Department (IMD) for the summer spell across Maharashtra.  
  > Before applying statistical models, data hygiene is critical. Using the Interquartile Range (IQR) method, where $IQR = Q_3 - Q_1 = 3.90^\circ\text{C}$, we identified extreme temperature outliers beyond the upper fence $Q_3 + 1.5 \times IQR = 46.1^\circ\text{C}$.  
  > To structure this continuous data, I generated a 7-bin continuous frequency distribution table and the corresponding less-than Ogive curve you see here. The total frequency $\sum f_i = 65$ exactly verifies our sample count. Now, Member 2 will explain the baseline dispersion."*

---

### Member 2: Descriptive Statistics & Dispersion Lead (Min 1:00 – 2:00)
- **Action on Screen:** Click on **Tab 3: "2. Descriptive Stats (M2)"**.
- **Script:**
  > *"Thank you Member 1. I am Member 2, leading Descriptive Statistics and Measures of Dispersion.  
  > As shown on the dashboard, our sample mean maximum temperature is $\bar{x} = 38.54^\circ\text{C}$, with a median of $38.40^\circ\text{C}$. Grouped mean calculated from class intervals is $38.23^\circ\text{C}$, demonstrating less than 0.8% grouping error.  
  > To measure temperature volatility, we calculated sample variance with Bessel's correction using $N-1 = 64$ degrees of freedom, yielding $s^2 = 9.95\ (^\circ\text{C})^2$ and standard deviation $s = 3.15^\circ\text{C}$.  
  > Most importantly, our Coefficient of Variation is $CV = \frac{s}{\bar{x}} \times 100\% = 8.18\%$. While an 8% CV shows relative baseline stability, our standard deviation of $3.15^\circ\text{C}$ proves that a single $2\sigma$ departure pushes regional temperatures beyond $44.8^\circ\text{C}$, causing severe heat emergencies. Member 3 will now explain the probability modeling."*

---

### Member 3: Probability & Normal Distribution Specialist (Min 2:00 – 3:15)
- **Action on Screen:** Click on **Tab 4: "3. Normal Distribution (M3)"**. Move the interactive threshold slider to $40.0^\circ\text{C}$ and $42.0^\circ\text{C}$.
- **Script:**
  > *"I am Member 3, responsible for Extreme Temperature Probability and Gaussian Modeling.  
  > We fitted a Normal Distribution $\mathcal{N}(\mu = 38.54, \sigma = 3.15)$ to the daily maximum temperatures.  
  > To quantify disaster risk, we transform temperature into the Standard Normal Variable $Z = \frac{X - \mu}{\sigma}$.  
  > For the IMD Heatwave threshold of $40^\circ\text{C}$, the $Z$-score is $+0.46$, giving an exceedance probability $P(X \ge 40^\circ\text{C}) = 1 - \Phi(0.46) = 32.15\%$. That means approximately one in every three summer days is statistically at risk.  
  > For the Severe Heatwave threshold of $42^\circ\text{C}$, $Z = +1.10$, yielding $P(X \ge 42^\circ\text{C}) = 13.60\%$.  
  > Notice on our interactive graph how the shaded critical right-tail area dynamically shifts as I adjust the threshold slider. Now Member 4 will address conditional risk and sensor reliability."*

---

### Member 4: Conditional Probability & Bayesian Inference Lead (Min 3:15 – 4:30)
- **Action on Screen:** Click on **Tab 5: "4. Bayesian Inference (M4)"**. Adjust the False Alarm Rate slider.
- **Script:**
  > *"I am Member 4, handling Conditional Probability and Bayesian Inference.  
  > Temperature alone does not cause heat mortality—humidity prevents sweat evaporation. As shown in our joint contingency table, the conditional probability of a heatwave given high humidity ($>60\%$) is $P(\text{Heatwave} \mid \text{High Humidity}) = \frac{n(\text{Both})}{n(\text{High Hum})}$.  
  > Next, in an AI-driven smart city, IoT meteorological sensors trigger automated alarms. However, sensors produce false alarms. Using Bayes' Theorem:  
  > $P(H \mid S) = \frac{P(S \mid H) P(H)}{P(S)}$  
  > With a prior heatwave probability $P(H) = 29.2\%$, sensor sensitivity of 92%, and false alarm rate of 8%, an automated alarm dramatically elevates our posterior belief from $29.2\%$ to **$82.6\%$**! This prevents disaster management teams from responding to false alarms. Member 5 will now present time series persistence."*

---

### Member 5: Time Series & Random Process Lead (Min 4:30 – 5:30)
- **Action on Screen:** Click on **Tab 6: "5. Random Process (M5)"**. Hover over the Autocorrelation Correlogram.
- **Script:**
  > *"Thank you Member 4. I am Member 5, leading Random Process and Time Series Modeling.  
  > In real engineering systems, temperatures are not independent and identically distributed (i.i.d.) random variables; they constitute a discrete-time random process $\{X_t\}$.  
  > We calculated the Sample Autocorrelation Function (ACF) up to lag 7. As seen on the correlogram, the lag-1 autocorrelation is $r_1 = +0.7682$, which vastly exceeds the 95% Bartlett confidence bound of $\pm \frac{1.96}{\sqrt{65}} = \pm 0.243$.  
  > This proves thermal memory—if today is extremely hot, there is a 77% linear correlation that tomorrow will also remain excessively hot.  
  > Furthermore, our 7-day rolling window demonstrates seasonal non-stationarity, and our streak detector identified two sustained heatwave spells lasting 4 and 5 consecutive days. Member 6 will now demonstrate our AI Early Warning System."*

---

### Member 6: AI Decision Engine & UI Lead (Min 5:30 – 6:45)
- **Action on Screen:** Click on **Tab 1: "🚨 Live AI Early Warning"**. In the sidebar, drag the **Temperature Offset slider to +4.5°C** to show the live trigger flipping from GREEN to RED!
- **Script:**
  > *"I am Member 6, responsible for the AI Decision Engine and System Architecture.  
  > We synthesized all statistical indicators into an automated multi-tier Early Warning System adhering to IMD and NDMA protocols: Green, Yellow, Orange, and Red.  
  > Watch as I simulate an incoming heatwave using our live telemetry slider: as I increase the temperature offset by $+4.5^\circ\text{C}$, the system dynamically evaluates the tail exceedance probability ($>35\%$), the apparent heat index ($>52^\circ\text{C}$), and streak persistence.  
  > The system immediately elevates the alert to **RED ALERT** and outputs automated civil directives: activating hospital heatstroke ICUs, enforcing afternoon construction bans, and deploying water tankers.  
  > In conclusion, our system proves that rigorous statistics transforms raw meteorological telemetry into life-saving engineering decisions. Thank you, and we are ready for individual viva questions!"*

---

## 🎯 30 Targeted Individual Viva Questions & Answers

### For Member 1 (Data Engineering Lead)
1. **Q: Why did you use the IQR method instead of standard deviation for outlier detection?**  
   *A:* "Standard deviation and mean are themselves heavily sensitive to extreme outliers. The IQR method uses quartiles ($Q_1$ and $Q_3$), which are non-parametric and robust against extreme values."
2. **Q: What is the formula for the class mark ($x_i$)?**  
   *A:* "Class mark is the arithmetic midpoint of the class interval: $x_i = \frac{\text{Lower Limit} + \text{Upper Limit}}{2}$."
3. **Q: How did you select 7 class intervals?**  
   *A:* "Using Sturges' Rule: $k = 1 + 3.322 \log_{10}(N)$. For $N = 65$, $k \approx 1 + 3.322(1.81) \approx 7$ bins."
4. **Q: What does a less-than Ogive represent?**  
   *A:* "It plots the upper class boundary against cumulative frequency, showing how many observations fall below any given temperature threshold."
5. **Q: What is the source of your dataset?**  
   *A:* "India Meteorological Department (IMD) open surface weather records and Open Government Data Platform India (`data.gov.in`)."

### For Member 2 (Descriptive Statistics Lead)
6. **Q: Why do we use $N-1$ in sample variance instead of $N$?**  
   *A:* "Using $N-1$ applies Bessel's correction to eliminate bias in estimating the true population variance $\sigma^2$ from a finite sample."
7. **Q: What is the Coefficient of Variation ($CV$) and why is it unitless?**  
   *A:* "$CV = \frac{s}{\bar{x}} \times 100\%$. Because both standard deviation and mean share the same unit ($^\circ\text{C}$), dividing them cancels the units, allowing relative comparison of variability across different cities or scales."
8. **Q: Why is the grouped mean slightly different from the ungrouped mean?**  
   *A:* "Grouped mean assumes all values within a class interval are concentrated at the class midpoint ($x_i$), introducing a minor grouping approximation error."
9. **Q: What is the formula for grouped median?**  
   *A:* "$M_d = L + \left[ \frac{\frac{N}{2} - cf}{f} \right] \times h$, where $L$ is lower limit of median class, $cf$ is previous cumulative frequency, $f$ is frequency, and $h$ is class width."
10. **Q: If temperature increases uniformly by $2^\circ\text{C}$ every day, what happens to variance?**  
    *A:* "Variance remains unchanged, because adding a constant shifts the mean by $+2^\circ\text{C}$, so deviations $(x_i - \bar{x})$ remain identical."

### For Member 3 (Probability & Normal Distribution Specialist)
11. **Q: What is the Standard Normal Variable ($Z$)?**  
    *A:* "$Z = \frac{X - \mu}{\sigma}$. It transforms any normal variable $X \sim \mathcal{N}(\mu, \sigma^2)$ into a standard normal distribution $Z \sim \mathcal{N}(0, 1)$."
12. **Q: How do you calculate the probability $P(X \ge 40^\circ\text{C})$?**  
    *A:* "We compute $Z = \frac{40 - \mu}{\sigma}$, look up the cumulative distribution function $\Phi(Z)$, and subtract from 1: $P(X \ge 40) = 1 - \Phi(Z)$."
13. **Q: What is the Empirical Rule for a Normal Distribution?**  
    *A:* "$68.27\%$ of values fall within $\mu \pm 1\sigma$, $95.45\%$ within $\mu \pm 2\sigma$, and $99.73\%$ within $\mu \pm 3\sigma$."
14. **Q: Why might temperature deviate from a pure Normal distribution?**  
    *A:* "Temperatures exhibit positive skewness and kurtosis during heatwaves because extreme convective heat accumulation creates a heavy right tail."
15. **Q: What is the probability density function (PDF) of a Normal distribution?**  
    *A:* "$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2}$."

### For Member 4 (Conditional Probability & Bayesian Specialist)
16. **Q: State Bayes' Theorem formula.**  
    *A:* "$P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)} = \frac{P(B \mid A) P(A)}{P(B \mid A)P(A) + P(B \mid \neg A)P(\neg A)}$."
17. **Q: What is the difference between prior and posterior probability?**  
    *A:* "Prior probability $P(H)$ is our initial belief before observing new evidence. Posterior probability $P(H \mid S)$ is the updated belief after observing sensor evidence $S$."
18. **Q: What is conditional probability?**  
    *A:* "$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$, representing the probability of event $A$ occurring given that event $B$ has already occurred."
19. **Q: Why is high humidity dangerous during a heatwave?**  
    *A:* "High humidity prevents evaporative cooling of sweat, drastically elevating the apparent Heat Index and biological core temperature."
20. **Q: How does a false alarm rate of 8% affect sensor reliability?**  
    *A:* "It means in 8% of non-heatwave days, the sensor mistakenly triggers an alert. Bayes' theorem balances this false alarm rate against the true prior to give the real probability."

### For Member 5 (Time Series & Random Process Lead)
21. **Q: What is a Random Process?**  
    *A:* "A collection of random variables indexed by time: $\{X(t), t \in T\}$. For daily temperature, it is a discrete-parameter, continuous-state random process."
22. **Q: What does an autocorrelation $r_1 = +0.768$ indicate?**  
    *A:* "It indicates strong positive persistence; consecutive daily temperatures are strongly interdependent rather than random independent noise."
23. **Q: How do you calculate Bartlett's 95% confidence bounds for ACF?**  
    *A:* "$\text{CI}_{95\%} = \pm \frac{1.96}{\sqrt{N}}$. Any lag with $|r_k|$ exceeding this bound is statistically significant."
24. **Q: What is weak stationarity?**  
    *A:* "A random process is weakly stationary if its mean $\mathbb{E}[X_t] = \mu$ is constant over time, and its autocovariance depends only on the time lag $k$, not on absolute time $t$."
25. **Q: Did your temperature dataset exhibit stationarity?**  
    *A:* "No, it exhibited seasonal non-stationarity because rolling 7-day mean temperatures drifted upwards during summer heatwave spells."

### For Member 6 (AI Decision Engine & UI Lead)
26. **Q: How does the AI Early Warning System make decisions?**  
    *A:* "It uses a rule-based expert decision matrix that checks temperature thresholds ($40^\circ\text{C}, 42^\circ\text{C}, 45^\circ\text{C}$), exceedance probabilities ($P > 35\%$), apparent Heat Index, and streak duration to assign IMD color tiers."
27. **Q: What are the four IMD Heatwave Alert levels?**  
    *A:* "Green (Normal), Yellow (Heat Watch / Preparedness), Orange (Heat Alert / Warning), and Red (Severe Heatwave / Emergency Action)."
28. **Q: What engineering actions are triggered under a Red Alert?**  
    *A:* "Hospital heatstroke ICU wards activated, outdoor construction banned from 11:00 AM - 4:30 PM, emergency water tankers deployed, and power grid reserves boosted for air conditioning load."
29. **Q: What are the engineering limitations of this system?**  
    *A:* "Single-station telemetry ignores Urban Heat Island (UHI) microclimates, and Gaussian distribution slightly underestimates extreme tail events."
30. **Q: How does your web app fulfill the criteria 'Input/Data -> Statistical Method -> Result -> Engineering Decision'?**  
    *A:* "Input data is ingested via CSV -> processed through descriptive stats, Gaussian fitting, and Bayes' updates -> producing exceedance probabilities and ACF -> which directly trigger automated municipal directives in the decision engine."
