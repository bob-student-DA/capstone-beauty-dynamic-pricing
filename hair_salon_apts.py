import pandas as pd
pd.set_option("display.max_columns", None)

df = pd.read_csv("data/salon/appointments_anonymized.csv")

# --- Basic profile ---
print(df.shape)
df.info()
print("\nMissing values:\n", df.isnull().sum()[df.isnull().sum() > 0])
print(df.head())

# --- Convert timestamps ---
df["appt_dt"] = pd.to_datetime(df["appt_datetime_utc"])
df["booked_dt"] = pd.to_datetime(df["booked_datetime_utc"])

# --- Values for the D4 highlights ---
print("\nDate range:", df["appt_dt"].min(), "to", df["appt_dt"].max())
print("Weeks covered:", round((df["appt_dt"].max() - df["appt_dt"].min()).days / 7, 1))
print("\nStatus:\n", df["status"].value_counts())
print("\nProviders:\n", df["provider_pid"].value_counts())
print("\nBooking method:\n", df["booking_method"].value_counts())
print("\nUnique services:", df["services"].nunique())
print(df["services"].value_counts().head(15))
print("\nDeposit amounts:\n", df["deposit_amount"].value_counts())

# --- Validity checks ---
print("\nDuplicate appointment_hash:", df["appointment_hash"].duplicated().sum())
df["lead_days"] = (df["appt_dt"] - df["booked_dt"]).dt.days
print("Negative lead times:", (df["lead_days"] < 0).sum())
print("\nLead time (days):\n", df["lead_days"].describe())

# --- Date-shift check (day of week may be scrambled) ---
print("\nBookings by day of week (UTC):\n", df["appt_dt"].dt.day_name().value_counts())
print("\nBookings by hour (UTC):\n", df["appt_dt"].dt.hour.value_counts().sort_index())