import pandas as pd
import os

def process_stats(file_path="data/raw/player_game_logs.csv"):
    df = pd.read_csv(file_path)
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])

    relevant_stats = df[['Player', 'GAME_DATE', 'PTS', 'REB', 'AST']]
    avg_stats = relevant_stats.groupby('Player')[['PTS', 'REB', 'AST']].mean().reset_index()
    avg_stats = avg_stats.sort_values(by='PTS', ascending=False)

    os.makedirs("data/processed", exist_ok=True)
    avg_stats.to_csv("data/processed/player_avg_stats.csv", index=False)
    print("Processed data saved to data/processed/player_avg_stats.csv")

if __name__ == "__main__":
    process_stats()