# Digital Asset Security Monitoring Platform

A Python-based Security Operations Center (SOC) detection engine designed to monitor digital asset environments by analyzing authentication and transaction logs. The platform identifies suspicious behavior patterns such as account compromise, anomalous access, and potential asset exfiltration using time-based correlation and risk scoring.

---

## 🚀 Overview

Modern digital asset platforms face increasingly sophisticated threats, including account takeovers and rapid asset withdrawals following unauthorized access. This project simulates a real-world SOC detection pipeline that correlates multiple log sources to detect such threats.

The system processes:
- Authentication logs (login activity, IP addresses, geolocation)
- Wallet transaction logs (withdrawals, transfers, asset movements)

By combining these datasets, the platform detects high-risk behavioral patterns that would typically trigger alerts in enterprise security systems.

---

## 🔍 Key Features

### 1. Impossible Travel Detection
Identifies suspicious login behavior where a user appears to log in from geographically distant locations within an unrealistic timeframe.

### 2. Large Withdrawal Detection
Flags high-value transactions that exceed predefined thresholds, indicating potential financial risk.

### 3. Correlated Attack Detection (Core Feature)
Detects account compromise scenarios by correlating:
- Suspicious login events (e.g., from high-risk locations)
- Followed by large withdrawals within a defined time window

This mirrors real-world attack patterns such as:
> Account takeover → Immediate asset exfiltration

### 4. Time-Based Correlation Engine
Applies temporal logic to ensure alerts are only triggered when events occur within a realistic attack window (e.g., within 30 minutes).

### 5. Dynamic Risk Scoring System
Assigns severity and risk scores based on:
- Transaction size
- Behavioral context
- Correlation strength

---

## 🧠 Detection Logic

The platform combines multiple detection strategies:

| Detection Type         | Data Source        | Logic |
|----------------------|------------------|------|
| Impossible Travel     | Authentication   | Location change anomaly |
| Large Withdrawal      | Transactions     | Amount threshold |
| Correlated Attack     | Auth + Transactions | Login anomaly + withdrawal within time window |

---

## 🖥️ Sample Output
User       Type                 Severity   Score  Time Diff
alice      CORRELATED_ATTACK    HIGH       85     1.0
charlie    CORRELATED_ATTACK    MEDIUM     70     5.0

---

Each alert includes:
- User identity
- Detection type
- Severity level
- Risk score
- Time correlation window

---

## 🛠️ Technologies Used

- Python
- Pandas (data processing)
- Modular detection architecture

---

## ⚙️ Project Structure
digital-asset-security-monitoring-platform/
│
├── app/
│   ├── detections/
│   │   ├── impossible_travel.py
│   │   ├── large_withdrawal.py
│   │   ├── correlated_attack.py
│   │   └── init.py
│   └── main.py
│
├── data/
│   ├── auth_logs.csv
│   └── wallet_logs.csv
│
├── simulations/
│   └── load_logs.py
│
├── requirements.txt
└── README.md

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/digital-asset-security-monitoring-platform.git
cd digital-asset-security-monitoring-platform

Install dependencies:
pip install -r requirements.txt

Run the simulation:
python3 -m simulations.load_logs
```

---


## 🧩 Real-World Relevance

This project reflects real detection mechanisms used in:

- **Security Operations Centers (SOC)**
- **Financial fraud detection systems**
- **Cryptocurrency exchanges and custody platforms**
- **SIEM tools such as Splunk and Microsoft Sentinel**

---

## 🎯 Key Concepts Demonstrated

- **Log correlation across multiple data sources**
- **Behavioral anomaly detection**
- **Time-based attack pattern analysis**
- **Risk scoring and severity classification**
- **Modular detection pipeline design**
