import pandas as pd

def detect_correlated_attack(auth_df, wallet_df):
    alerts = []

    suspicious_locations = ["Russia", "Germany"]

    auth_df["timestamp"] = pd.to_datetime(auth_df["timestamp"])
    wallet_df["timestamp"] = pd.to_datetime(wallet_df["timestamp"])

    suspicious_logins = auth_df[
        (auth_df["event_type"] == "login_success") &
        (auth_df["location"].isin(suspicious_locations))
    ]

    withdrawals = wallet_df[wallet_df["event_type"] == "withdrawal_request"]

    for _, login in suspicious_logins.iterrows():
        user = login["user"]
        login_time = login["timestamp"]

        user_withdrawals = withdrawals[withdrawals["user"] == user]

        for _, wd in user_withdrawals.iterrows():
            wd_time = wd["timestamp"]
            time_diff = (wd_time - login_time).total_seconds() / 60

            if 0 <= time_diff <= 30:
                amount = float(wd["amount"])

                if amount >= 50:
                    severity = "CRITICAL"
                    risk_score = 95
                elif amount >= 20:
                    severity = "HIGH"
                    risk_score = 85
                elif amount >= 10:
                    severity = "MEDIUM"
                    risk_score = 70
                else:
                    continue

                alerts.append({
                    "user": user,
                    "type": "CORRELATED_ATTACK",
                    "login_location": login["location"],
                    "withdrawal_amount": amount,
                    "asset": wd["asset"],
                    "time_difference_min": round(time_diff, 2),
                    "timestamp": wd["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                    "severity": severity,
                    "risk_score": risk_score,
                    "description": f"Login from {login['location']} followed by withdrawal in {round(time_diff, 2)} mins"
                })

    return alerts