# Import necessary libraries for data handling and visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define a function to plot the top scorers from a processed stats CSV
def plot_top_scorers(file_path="data/processed/player_avg_stats.csv", top_n=15):
    # Read the processed player average stats data
    df = pd.read_csv(file_path)

    # Take the top N players based on average points (assuming data is already sorted)
    top_df = df.head(top_n)

    # Set up the plot size
    plt.figure(figsize=(12, 8))

    # Create a horizontal bar plot of average points by player
    sns.barplot(x='PTS', y='Player', data=top_df, palette='viridis')

    # Add plot title and axis labels
    plt.title(f'Top {top_n} Players by Average Points per Game (2024–25)')
    plt.xlabel('Average Points')
    plt.ylabel('Player')

    # Adjust layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()

# Run the function if this script is executed directly
if __name__ == "__main__":
    plot_top_scorers()
