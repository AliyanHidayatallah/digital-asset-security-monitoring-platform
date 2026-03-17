import pandas as pd

def detect_impossible_travel(auth_df):
    alerts = []

    # Only look at successful logins
    logins = auth_df[auth_df["event_type"] == "login_success"]

    # Sort by user and time
    logins = logins.sort_values(by=["user", "timestamp"])

    # Loop through users
    for user in logins["user"].unique():
        user_logins = logins[logins["user"] == user]

        previous_location = None

        for _, row in user_logins.iterrows():
            current_location = row["location"]

            if previous_location and current_location != previous_location:
                alerts.append({
                    "user": user,
                    "type": "IMPOSSIBLE_TRAVEL",
                    "previous_location": previous_location,
                    "current_location": current_location,
                    "timestamp": row["timestamp"],
                    "severity": "HIGH",
                    "description": f"{user} logged in from {previous_location} then {current_location}"
                })

            previous_location = current_location

    return alerts