import pandas as pd

print("SCRIPT STARTED")

csv_path = "data/raw/Market_trends.csv"
output_path = "data/cleaned/market_trends_cleaned.csv"

# --------------------------------------------------
# 1. Load CSV WITHOUT headers
# --------------------------------------------------
df_raw = pd.read_csv(csv_path, header=None)

print("RAW PREVIEW:")
print(df_raw.head(10))

# --------------------------------------------------
# 2. Find the REAL header row (contains 'Commodity')
# --------------------------------------------------
header_row_index = None

for i in range(len(df_raw)):
    row_text = " ".join(
        str(x) for x in df_raw.iloc[i].values if pd.notna(x)
    )
    if "Commodity" in row_text:
        header_row_index = i
        break

if header_row_index is None:
    raise ValueError("❌ Could not find header row")

print(f"✅ Header row found at index {header_row_index}")
print("HEADER:", df_raw.iloc[header_row_index])
print("SUBHEADER:", df_raw.iloc[header_row_index + 1])

# --------------------------------------------------
# 3. MERGE main header + sub header
# --------------------------------------------------
main_header = df_raw.iloc[header_row_index]
sub_header  = df_raw.iloc[header_row_index + 1]

final_columns = []
for main, sub in zip(main_header, sub_header):
    if pd.notna(main):
        final_columns.append(str(main))
    else:
        final_columns.append(str(sub))

# Slice actual DATA
df = df_raw.iloc[header_row_index + 2:].reset_index(drop=True)
df.columns = final_columns

# --------------------------------------------------
# 4. Normalize column names
# --------------------------------------------------
df.columns = (
    df.columns
      .astype(str)
      .str.strip()
      .str.lower()
      .str.replace("\xa0", "", regex=False)
      .str.replace(" ", "_")
)

print("COLUMNS AFTER NORMALIZATION:")
print(df.columns)

# --------------------------------------------------
# 5. Drop junk rows
# --------------------------------------------------
df = df[df["commodity"].notna()]

# Replace dash values
df = df.replace({"-": pd.NA, "–": pd.NA, "—": pd.NA})

# --------------------------------------------------
# 6. PRICE columns → LONG format
# --------------------------------------------------
price_cols = [c for c in df.columns if c.startswith("price_on")]

print("PRICE COLUMNS:", price_cols)

df_long = df.melt(
    id_vars=["commodity_group", "commodity"],
    value_vars=price_cols,
    var_name="date",
    value_name="price"
)

print("DEBUG after melt:", len(df_long))
print(df_long.head())

# --------------------------------------------------
# 7. Clean numeric values
# --------------------------------------------------
df_long["price"] = pd.to_numeric(df_long["price"], errors="coerce")
df_long = df_long.dropna(subset=["price"])

# --------------------------------------------------
# 8. Parse date from column name
# --------------------------------------------------
df_long["date"] = df_long["date"].str.replace("price_on_", "", regex=False)

df_long["date"] = pd.to_datetime(
    df_long["date"],
    format="%d_%b,_%Y",
    errors="coerce"
)

df_long = df_long.dropna(subset=["date"])

# --------------------------------------------------
# 9. SAVE (THIS IS THE ONE THAT MATTERS)
# --------------------------------------------------
df_long.to_csv(output_path, index=False)

print("✅ CLEANED DATA SAVED")
print("✅ FINAL ROW COUNT:", len(df_long))
print(df_long.head())