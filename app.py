import streamlit as st
import re

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Cyber Fraud Detection", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #0f172a;
    }

    h1 {
        color: #38bdf8;
        text-align: center;
    }

    .safe {
        color: #22c55e;
        font-weight: bold;
    }

    .suspicious {
        color: #facc15;
        font-weight: bold;
    }

    .scam {
        color: #ef4444;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>🛡️ CYBER FRAUD DETECTION DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("### 🔐 Real-time Risk Analysis for Cyber Crime Prevention")

# ---------- FUNCTION ----------
def calculate_risk(text):
    text_lower = text.lower()
    score = 0
    detected = []

    # ---------- ENGLISH KEYWORDS ----------
    keywords = {
        "otp": 40,
        "urgent": 25,
        "immediately": 20,
        "click": 20,
        "verify": 25,
        "password": 35,
        "bank": 15,
        "account": 15,
        "send": 30,
        "money": 25,
        "win": 30,
        "prize": 30,
        "upi": 40,
        "pin": 40,
        "payment": 30,
        "received": 20,
        "reward": 25,
        "offer": 20,
        "kyc": 25,
        "lottery": 30
    }

    # ---------- TELUGU KEYWORDS ----------
    telugu_keywords = {
        "otp": 40,
        "వెంటనే": 25,
        "బ్యాంక్": 20,
        "ఖాతా": 20,
        "క్లిక్": 20,
        "బహుమతి": 30,
        "వివరాలు": 25,
        "డబ్బు": 25
    }

    # ---------- KEYWORD MATCH ----------
    for word, value in keywords.items():
        if word in text_lower:
            score += value
            detected.append(word)

    for word, value in telugu_keywords.items():
        if word in text_lower:
            score += value
            detected.append(word)

    # ---------- URL DETECTION ----------
    if re.search(r'http[s]?://', text_lower):
        score += 30
        detected.append("suspicious_link")

    # ---------- SMART PATTERNS ----------
    if "upi" in text_lower and "pin" in text_lower:
        score += 40
        detected.append("upi_fraud_pattern")

    if "click" in text_lower and ("otp" in text_lower or "password" in text_lower):
        score += 30
        detected.append("phishing_pattern")

    if "won" in text_lower or "lottery" in text_lower:
        score += 25
        detected.append("lottery_scam")

    # ---------- FINAL SCORE ----------
    score = min(score, 100)

    # ---------- CLASSIFICATION ----------
    if score >= 75:
        level = "SCAM 🚨"
        css_class = "scam"
    elif score >= 40:
        level = "SUSPICIOUS ⚠️"
        css_class = "suspicious"
    else:
        level = "SAFE ✅"
        css_class = "safe"

    return score, level, css_class, detected


# ---------- LAYOUT ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📥 Input Message")
    user_input = st.text_area("", height=150)

    analyze = st.button("🔍 Analyze Message")

with col2:
    st.markdown("### ℹ️ System Info")
    st.info("Detects fraud patterns like OTP scams, phishing links, UPI fraud, and urgency-based attacks.")

# ---------- OUTPUT ----------
if analyze and user_input:
    score, level, css_class, keywords = calculate_risk(user_input)

    st.markdown("---")
    st.markdown("## 📊 Analysis Dashboard")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("Risk Score", f"{score}%")

    with col4:
        st.progress(score)

    with col5:
        st.markdown(f"<h3 class='{css_class}'>{level}</h3>", unsafe_allow_html=True)

    st.markdown("---")

    col6, col7 = st.columns(2)

    with col6:
        st.markdown("### 🔍 Detected Keywords / Patterns")
        st.write(keywords)

    with col7:
        st.markdown("### 📄 Input Text")
        st.write(user_input)

    st.markdown("---")

    # ---------- AI INSIGHT ----------
    st.markdown("### 🧠 AI Insight")

    if score >= 75:
        st.error("⚠️ High Risk: Strong scam indicators detected (UPI / OTP / phishing patterns).")
    elif score >= 40:
        st.warning("⚠️ Medium Risk: Suspicious patterns detected. Be cautious.")
    else:
        st.success("✅ Safe: No major fraud patterns detected.")

    # ---------- EXTRA EXPLANATION ----------
    st.write(f"🔎 Patterns Identified: {keywords}")

    st.markdown("---")

    # ---------- SAFETY TIP ----------
    st.warning("💡 Never share OTP, passwords, UPI PIN, or bank details with anyone.")