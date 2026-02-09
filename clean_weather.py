import pandas as pd

print("SCRIPT STARTED")
csv_path = "data/raw/weather.csv"

df = pd.read_csv(csv_path)

print("CSV LOADED")
print(df.head())
print(df.info())

print("\nCOLUMNS:")
print(df.columns)

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nSUMMARY:")
print(df.describe(include="all"))

df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

print(df.columns)

df["precip"] = (
    df["precip"]
      .astype(str)
      .str.replace("mm", "", regex=False)
      .astype(float)
)

df["temp"] = df["temp"].astype(float)

df["temp"] = (df["temp"] - 32) * 5 / 9

df["humidity"] = df["humidity"].astype(float)
df = df[df["humidity"].between(0, 100)]

df = df.dropna()

columns_to_drop = [
    "feelslikemax",
    "feelslikemin",
    "feelslike",
    "dew",
    "precipcover",
    "snow",
    "solarradiation",
    "snowdepth",
    "windgust",
    "winddir",
    "solarenergy",
    "moonphase"
]

df = df.drop(columns=columns_to_drop, errors="ignore")

print(df.columns)

last_15_days_df = df.tail(15)

df["timestamp"] = pd.date_range(
    end=pd.Timestamp.today(),
    periods=len(df),
    freq="D"
)

output_path = "data/cleaned/weather_cleaned.csv"
df.to_csv(output_path, index=False)

print("✅ Cleaned CSV saved to:", output_path)
