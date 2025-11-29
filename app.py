import streamlit as st
import pandas as pd
data = {
    "Home Team": [
        "Chesterfield", "Sutton", "York", "Bedford", "Buxton",
        "Macclesfield", "Radcliffe", "Dover", "Burgess", "Canvey",
        "Halesowen", "Leiston", "Redditch", "Dorchester", "Farnham",
        "Tiverton", "Weymouth"
    ],
    "H 3.5": [
        50, 40, 90, 50, 33,
        38, 50, 56, 43, 57,
        44, 67, 50, 56, 50,
        29, 33
    ],
    "OH 3.5": [
        47, 45, 65, 37, 33,
        44, 47, 37, 39, 35,
        39, 42, 33, 44, 56,
        47, 42
    ],
    "A 3.5": [
        38, 70, 50, 33, 67,
        56, 38, 38, 43, 44,
        33, 62, 45, 44, 67,
        44, 38
    ],
    "OA 3.5": [
        41, 50, 55, 47, 68,
        35, 44, 44, 56, 47,
        41, 47, 47, 61, 39,
        44, 44
    ],
    "ODD": [
        2.60, 2.05, 1.65, 2.30, 2.15,
        2.85, 2.40, 2.15, 2.67, 2.65,
        2.50, 2.50, 2.72, 2.65, 2.12,
        2.30, 2.52
    ],
    "L8 HA 3.5": [
        44, 56, 50, 44, 56,
        44, 50, 44, 50, 38,
        50, 50, 38, 56, 56,
        56, 56
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

