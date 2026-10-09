"""
Module 6: AI Decision Engine & Early Warning System
Owned by: Member 6 (AI Decision Engine & UI Lead)
Topic: Rule-based AI Early Warning, IMD Alert Tiers, Actionable Civil & Health Decisions
"""

def evaluate_heatwave_risk(current_temp, prob_exceed_40, prob_exceed_42, heat_index, streak_days=0):
    """
    Synthesize statistical inputs to compute an authoritative AI Early Warning Tier.
    Returns: Alert Color, Alert Name, Severity Score (1-4), Rationale, and Municipal Directives.
    """
    # Decision Matrix logic based on IMD & National Disaster Management Authority (NDMA)
    if current_temp >= 44.0 or prob_exceed_42 >= 0.35 or heat_index >= 52.0 or streak_days >= 4:
        tier = "RED"
        title = "Severe Heatwave Warning (Extreme Emergency)"
        severity = 4
        color = "#DC2626"
        rationale = (
            f"Critical thermal threshold breached. Current Temp ({current_temp:.1f}°C) or "
            f"Heat Index ({heat_index:.1f}°C) poses severe risk of heat stroke even with minimal exertion."
        )
        actions = [
            "🚨 Issue immediate Red Alert via municipal SMS and emergency broadcasts.",
            "🏥 Hospital Emergency Protocol: Activate dedicated air-conditioned heatstroke ICU wards.",
            "🚧 Labor Directives: Strict legal moratorium on all outdoor construction from 11:00 AM to 4:30 PM.",
            "💧 Water Utilities: Deploy high-capacity water tankers to high-density informal settlements.",
            "⚡ Power Grid Management: Ramp up spinning reserve to prevent transformer failure under peak cooling demand.",
            "🏫 Educational Institutions: Close primary schools or switch entirely to early morning shifts (ended by 11:00 AM)."
        ]
    elif current_temp >= 40.0 or prob_exceed_40 >= 0.40 or heat_index >= 45.0 or streak_days >= 2:
        tier = "ORANGE"
        title = "Heatwave Alert (Severe Action Required)"
        severity = 3
        color = "#EA580C"
        rationale = (
            f"High persistence detected. Temperature ({current_temp:.1f}°C) and Exceedance Probability "
            f"({prob_exceed_40*100:.1f}%) indicate sustained heatwave conditions for vulnerable populations."
        )
        actions = [
            "⚠️ Issue Orange Alert for vulnerable groups (infants, elderly, chronic illness patients).",
            "🏥 Hospitals: Stock emergency reserves of ORS, IV fluids, and ice packs in triage centers.",
            "💧 Municipal Services: Set up public drinking water kiosks ('Pyaaos') at bus terminals and railway stations.",
            "🕒 Adjust public park timings and advise citizens to avoid sun exposure between 12:00 PM and 3:30 PM.",
            "👷 Ensure mandatory shaded rest stations and continuous hydration for outdoor transit workers."
        ]
    elif current_temp >= 38.0 or prob_exceed_40 >= 0.15 or heat_index >= 40.0:
        tier = "YELLOW"
        title = "Heat Watch (Advisory & Preparedness)"
        severity = 2
        color = "#CA8A04"
        rationale = (
            f"Moderate heat conditions. Temperature ({current_temp:.1f}°C) is elevated with moderate "
            f"probability of extreme spikes. Precautionary monitoring active."
        )
        actions = [
            "🟡 Issue Yellow Advisory: Disseminate heat safety awareness on weather portals.",
            "💧 Pre-position municipal water distribution supplies.",
            "🩺 Primary healthcare centers on standby for early dehydration symptoms.",
            "👷 Employers encouraged to provide adequate drinking water and light ventilation."
        ]
    else:
        tier = "GREEN"
        title = "Normal (No Alert)"
        severity = 1
        color = "#16A34A"
        rationale = (
            f"Normal climatic conditions. Current Temp ({current_temp:.1f}°C) and Exceedance Probability "
            f"({prob_exceed_40*100:.1f}%) remain within safe seasonal baseline limits."
        )
        actions = [
            "✅ Standard seasonal monitoring continues.",
            "📊 Routine meteorological telemetry logging active."
        ]
        
    return {
        'tier': tier,
        'title': title,
        'severity': severity,
        'color': color,
        'rationale': rationale,
        'actions': actions
    }
