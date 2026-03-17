def detect_large_withdrawals(wallet_df, threshold=10):
    alerts = []

    withdrawals = wallet_df[wallet_df["event_type"] == "withdrawal_request"]

    for _, row in withdrawals.iterrows():
        if float(row["amount"]) >= threshold:
            alerts.append({
                "user": row["user"],
                "type": "LARGE_WITHDRAWAL",
                "wallet_address": row["wallet_address"],
                "destination_address": row["destination_address"],
                "amount": float(row["amount"]),
                "asset": row["asset"],
                "timestamp": row["timestamp"],
                "severity": "HIGH",
                "description": f"Large withdrawal detected: {row['amount']} {row['asset']} by {row['user']}"
            })

    return alerts