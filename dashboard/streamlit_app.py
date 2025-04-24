# Import necessary libraries
import streamlit as st                      # Streamlit for creating web-based dashboards
import pandas as pd                         # Pandas for loading and handling data
import seaborn as sns                       # Seaborn for styled visualizations
import matplotlib.pyplot as plt             # Matplotlib for plotting

# Set the title of the Streamlit dashboard
st.title("NBA 2024–25 Stats Dashboard")

# Load the processed player average stats from a CSV file
df = pd.read_csv("data/processed/player_avg_stats.csv")

# Display the entire DataFrame as a scrollable table on the page
st.write("### Average Player Stats")
st.dataframe(df)

# Display a header and a chart showing the top 15 scorers
st.write("### Top 15 Scorers")

# Get the top 15 players based on average points per game
top_df = df.head(15)

# Create a figure and axis object for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar plot of average points by player
sns.barplot(x='PTS', y='Player', data=top_df, palette='viridis', ax=ax)

# Display the plot within the Streamlit app
st.pyplot(fig)
