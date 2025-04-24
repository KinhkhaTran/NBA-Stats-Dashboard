import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_scorers(file_path="data/processed/player_avg_stats.csv", top_n=15):
    df = pd.read_csv(file_path)
    top_df = df.head(top_n)

    plt.figure(figsize=(12, 8))
    sns.barplot(x='PTS', y='Player', data=top_df, palette='viridis')
    plt.title(f'Top {top_n} Players by Average Points per Game (2024–25)')
    plt.xlabel('Average Points')
    plt.ylabel('Player')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_top_scorers()