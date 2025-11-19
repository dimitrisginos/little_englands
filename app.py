import streamlit as st
import pandas as pd

# ---- DATASET ----
data = {
    "Home Team": [
        "Real Bedford","Spalding","Uxbridge","Royston","Gosport","Merthyr",
        "Stourbridge","Bishops","Ramsgate","Potters Bar","Havant","Cray Valley",
        "St. Albans","Dulwich","Slough","Walton"
    ],
    "H 3.5": [29,67,50,38,71,62,50,56,30,62,60,33,17,56,50,43],
    "OH 3.5": [47,53,44,35,56,65,50,47,56,53,50,41,36,39,44,36],
    "A 3.5": [62,38,67,75,50,50,25,50,25,43,50,43,67,43,29,43],
    "OA 3.5": [41,41,57,50,40,24,35,29,40,27,41,47,44,38,38,38],
    "ODD": [2.62,2.50,2.32,2.65,2.25,2.42,2.72,2.60,2.50,2.67,2.22,2.52,2.37,2.32,2.15,2.15],
    "L8 HA 3.5": [63,56,56,50,63,50,44,50,44,32,56,38,50,44,50,50],
}

df = pd.DataFrame(data)

# ---- CALCULATIONS ----
df["O 3.5 IND"] = (
    ((df["H 3.5"] + df["A 3.5"]) / 2) * 0.25 +
    ((df["OH 3.5"] + df["OA 3.5"]) / 2) +
    (df["L8 HA 3.5"] * 0.25)
)

df["INDEX"] = df["O 3.5 IND"] * df["ODD"]

# ---- SORTING ----
df = df.sort_values("O 3.5 IND", ascending=False)

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

