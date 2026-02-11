import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

print("Loading cleaned weather data...")

df = pd.read_csv("data/cleaned/weather_cleaned.csv")

if "timestamp" not in df.columns:
    raise ValueError("Missing 'timestamp' column")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

# Create numeric time index
df["time_index"] = np.arange(len(df))

# Features to predict
features = ["temp", "precip", "precipprob", "humidity", "cloudcover"]

for col in features:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

models = {}

# Train separate regression model for each feature
for feature in features:
    X = df[["time_index"]]
    y = df[feature]

    model = LinearRegression()
    model.fit(X, y)
    models[feature] = model

# ---------------------------------------------
# Predict next 7 time steps
# ---------------------------------------------
last_index = df["time_index"].max()
future_indices = np.arange(last_index + 1, last_index + 8)

future_dates = pd.date_range(
    start=df["timestamp"].max() + pd.Timedelta(days=1),
    periods=7
)

forecast_data = {"timestamp": future_dates}

for feature in features:
    predictions = models[feature].predict(future_indices.reshape(-1, 1))
    forecast_data[feature] = predictions

forecast_df = pd.DataFrame(forecast_data)

print("\n🔮 NEXT 7 DAY WEATHER FORECAST:")
print(forecast_df)

forecast_df.to_csv(
    "data/cleaned/next_week_weather_forecast.csv",
    index=False
)

print("\n✅ Forecast saved successfully.")