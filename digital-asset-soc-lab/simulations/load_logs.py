import pandas as pd

from app.detections.impossible_travel import detect_impossible_travel
from app.detections.large_withdrawal import detect_large_withdrawals
from app.detections.correlated_attack import detect_correlated_attack

auth_df = pd.read_csv("data/auth_logs.csv")
wallet_df = pd.read_csv("data/wallet_logs.csv")

print("=== Authentication Logs ===")
print(auth_df)
print()

print("=== Wallet Logs ===")
print(wallet_df)
print()

impossible_travel_alerts = detect_impossible_travel(auth_df)
large_withdrawal_alerts = detect_large_withdrawals(wallet_df)
correlated_attack_alerts = detect_correlated_attack(auth_df, wallet_df)

print("=== Impossible Travel Alerts ===")
for alert in impossible_travel_alerts:
    print(alert)

print()
print("=== Large Withdrawal Alerts ===")
for alert in large_withdrawal_alerts:
    print(alert)

print()
print("\n=== Correlated Attack Alerts ===")
print(f"{'User':<10} {'Type':<20} {'Severity':<10} {'Score':<5} {'Time Diff':<10}")

for alert in correlated_attack_alerts:
    print(f"{alert['user']:<10} {alert['type']:<20} {alert['severity']:<10} {alert['risk_score']:<5} {alert['time_difference_min']:<10}")