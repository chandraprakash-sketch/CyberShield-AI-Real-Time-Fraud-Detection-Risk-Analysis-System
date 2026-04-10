# 🛡️ CyberShield AI – Real-Time Fraud Detection Dashboard

## 🚀 Overview

CyberShield AI is a **Streamlit-based real-time cyber fraud detection system** that analyzes user-provided messages and identifies potential scam patterns using rule-based AI logic.

The system evaluates text inputs for:

* Phishing attempts
* OTP fraud
* UPI scams
* Suspicious links
* Urgency-based manipulation tactics

It provides a **risk score, classification, and actionable insights** to help users stay protected.

---

## 🎯 Key Features

* 🔍 **Real-Time Message Analysis**
* 📊 **Risk Scoring System (0–100%)**
* 🚨 **Fraud Classification**

  * SAFE ✅
  * SUSPICIOUS ⚠️
  * SCAM 🚨
* 🌐 **Multilingual Detection**

  * English + Telugu support
* 🔗 **URL Detection (Phishing Links)**
* 🧠 **Pattern-Based AI Logic**
* 📈 **Interactive Dashboard (Streamlit UI)**

---

## 🧠 How It Works

The system uses a **rule-based scoring algorithm**:

### 1. Keyword Detection

* Detects fraud-related keywords like:

  * OTP, UPI, password, bank, lottery, etc.

### 2. Multilingual Analysis

* Supports Telugu fraud keywords such as:

  * వెంటనే, బ్యాంక్, ఖాతా, డబ్బు

### 3. Pattern Recognition

* UPI + PIN → High-risk fraud pattern
* Click + OTP/Password → Phishing
* Lottery/Win → Scam

### 4. URL Detection

* Identifies suspicious links (`http/https`)

### 5. Risk Classification

| Score Range | Category      |
| ----------- | ------------- |
| 0–39        | SAFE ✅        |
| 40–74       | SUSPICIOUS ⚠️ |
| 75–100      | SCAM 🚨       |

---

## 🛠️ Tech Stack

* **Python 3**
* **Streamlit**
* **Regex (re module)**
* **Rule-Based AI Logic**

---

## 📂 Project Structure

```
📦 CyberShield-AI
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
streamlit run app.py
```

---

## 📊 Sample Use Cases

* Detect phishing SMS or emails
* Identify fake lottery messages
* Analyze suspicious WhatsApp texts
* Prevent UPI / banking fraud

---

## 🧠 AI Insight Example

* High score → 🚨 Strong scam indicators
* Medium score → ⚠️ Suspicious activity
* Low score → ✅ Safe message

---

## 🔐 Security Awareness

> Never share OTP, passwords, UPI PIN, or bank details with anyone.

---

## 🚀 Future Enhancements

* 🤖 Machine Learning / NLP model integration
* 🌍 More regional language support
* 📱 Mobile app version
* 🔗 API-based fraud detection service

---

## 👨‍💻 Author

**Chandra Prakash**

---

## ⭐ Contribution

Feel free to fork this project, raise issues, or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.
