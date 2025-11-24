import streamlit as st
import pandas as pd

# ---- DATASET ----
data = {
    "Home Team": [
        "Stourbridge", "Gosport", "Gloucester", "Southport", "Poole", "Darlington", "Bishops", "Spalding"
    ],
    "H 3.5": [
        57, 75, 44, 56, 25, 56, 50, 57],
    "OH 3.5": [
        53, 59, 35, 28, 40, 44, 44, 50],
    "A 3.5": [67, 44, 71, 50, 56, 56, 33, 44],
    "OA 3.5": [47, 39, 60, 50, 44, 33, 39, 28],
    "O 3.5 IND": [81.3, 79.6, 75.9, 66.3, 66.1, 65.0, 64.4, 61.1],
    "ODD": [2.67, 2.35, 2.32, 2.62, 2.27, 2.42, 2.60, 2.42],
    "L8 HA 3.5": [63, 63, 56, 56, 56, 50, 50, 38]
}


df = pd.DataFrame(data)

# ---- CALCULATIONS ----
df["O 3.5 IND"] = (
    ((df["H 3.5"] + df["A 3.5"]) / 2) * 0.25 +
    ((df["OH 3.5"] + df["OA 3.5"]) / 2) +
    (df["L8 HA 3.5"] * 0.25)
)

df["INDEX"] = df["O 3.5 IND"] * df["ODD"]

filtered_df = df[
    (df["H 3.5"] >= 25) &
    (df["A 3.5"] >= 25) &
    (df["OH 3.5"] >= 25) &
    (df["OA 3.5"] >= 25) &
    (df["INDEX"] >= 140)
]

# ---- SORTING ----
df = filtered_df.sort_values("O 3.5 IND", ascending=False)

# ---- STREAMLIT UI ----
st.title("Yindex 2.0")

st.write("Insert how many picks you want to see")

# User input
n = st.number_input("How many picks?", min_value=1, value=5)

# If user enters too large a number → return all teams
n = min(n, len(df))

# Select top N teams
top_df = df.head(int(n))

# Show result
st.subheader("Top Picks:")
for team in top_df["Home Team"]:
    st.write(team)

