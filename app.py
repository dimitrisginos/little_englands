import streamlit as st
import pandas as pd
data = {
    "Home Team": [
        "Fylde", "Stourbridge", "Gosport", "Folkestone", "Ramsgate",
        "Potters Bar", "Havant", "Hyde", "Needham Market", "Dorchester"
    ],
    "H 3.5": [
        50, 50, 78, 57, 27,
        67, 43, 44, 40, 60
    ],
    "OH 3.5": [
        55, 53, 63, 39, 55,
        50, 44, 50, 35, 47
    ],
    "A 3.5": [
        60, 56, 50, 70, 56,
        40, 50, 30, 60, 33
    ],
    "OA 3.5": [
        65, 50, 35, 58, 39,
        45, 44, 37, 45, 33
    ],
    "ODD": [
        1.75, 2.72, 2.25, 2.02, 2.20,
        2.30, 2.37, 2.60, 2.52, 2.70
    ],
    "L8 HA 3.5": [
        63, 75, 56, 50, 56,
        38, 44, 50, 44, 44
    ]
}

df = pd.DataFrame(data)


# Calculate O 3.5 IND
df["O 3.5 IND"] = (
    ((df["H 3.5"] + df["A 3.5"]) / 2) * 0.25 +
    ((df["OH 3.5"] + df["OA 3.5"]) / 2) +
    (df["L8 HA 3.5"] * 0.25)
)

# Calculate INDEX
df["INDEX"] = df["O 3.5 IND"] * df["ODD"]

# Filter based on your conditions
filtered_df = df[
    (df["H 3.5"] >= 25) &
    (df["A 3.5"] >= 25) &
    (df["OH 3.5"] >= 25) &
    (df["OA 3.5"] >= 25) &
    (df["INDEX"] >= 150)
]

df = filtered_df.sort_values("O 3.5 IND", ascending=False)

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

