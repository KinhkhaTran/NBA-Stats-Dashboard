import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("NBA 2024–25 Stats Dashboard")
df = pd.read_csv("data/processed/player_avg_stats.csv")

st.write("### Average Player Stats")
st.dataframe(df)

st.write("### Top 15 Scorers")
top_df = df.head(15)
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='PTS', y='Player', data=top_df, palette='viridis', ax=ax)
st.pyplot(fig)