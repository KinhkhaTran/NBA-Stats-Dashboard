"""
process_data.py
---------------
Cleans the raw game-log CSV and produces per-player season averages
(PTS, REB, AST) for quick exploratory work and visualization.

Author  : Kinhkha Tran
Created : 2025-05-01
Project : NBA 2024-25 Stats Dashboard
Usage   : python process_data.py
Input   : data/raw/player_game_logs.csv
Output  : data/processed/player_avg_stats.csv

Notes
-----
• Converts GAME_DATE to pandas datetime then selects core box-score stats. :contentReference[oaicite:2]{index=2}&#8203;:contentReference[oaicite:3]{index=3}
• Groups by player and sorts by average points scored.
• Creates `data/processed/` if it doesn’t exist.
"""

# Import pandas for data manipulation and os for file/directory operations
import pandas as pd
import os

def process_stats(file_path="data/raw/player_game_logs.csv"):
    # Read the raw player game log data from CSV
    df = pd.read_csv(file_path)

    # Convert the GAME_DATE column to datetime format for proper time handling
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])

    # Select only the relevant columns needed for analysis
    relevant_stats = df[['Player', 'GAME_DATE', 'PTS', 'REB', 'AST']]

    # Group the data by player and calculate the average points, rebounds, and assists
    avg_stats = relevant_stats.groupby('Player')[['PTS', 'REB', 'AST']].mean().reset_index()

    # Sort players in descending order by average points scored
    avg_stats = avg_stats.sort_values(by='PTS', ascending=False)

    # Create the processed data directory if it doesn't already exist
    os.makedirs("data/processed", exist_ok=True)

    # Save the processed average stats to a new CSV file
    avg_stats.to_csv("data/processed/player_avg_stats.csv", index=False)
    print("Processed data saved to data/processed/player_avg_stats.csv")

# Execute the function if this file is run directly
if __name__ == "__main__":
    process_stats()