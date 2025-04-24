# Import functions to get player info and game logs from nba_api
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

# Data manipulation and utilities
import pandas as pd
import time
import os

def fetch_top_player_logs(limit=30, season='2024-25'):
    # Get a list of all active NBA players
    all_players = players.get_active_players()

    # Container to store each player's game log DataFrame
    player_stats = []

    # Loop through the first 'limit' number of players
    for player in all_players[:limit]:
        try:
            # Fetch the player's game logs for the given season
            logs = playergamelog.PlayerGameLog(
                player_id=player['id'],
                season=season,
                season_type_all_star='Regular Season'
            )
            # Get the first (and only) DataFrame from the result
            df = logs.get_data_frames()[0]

            # Add a column with the player's name for easier grouping later
            df['Player'] = player['full_name']

            # Append the DataFrame to our list
            player_stats.append(df)

            # Log success
            print(f"Fetched data for {player['full_name']}")

            # Pause to respect API rate limits
            time.sleep(1)

        except Exception as e:
            # Print error if data retrieval fails for a player
            print(f"Error fetching {player['full_name']}: {e}")

    # Combine all player DataFrames into one (excluding empty ones just in case)
    all_stats = pd.concat([df for df in player_stats if not df.empty])

    # Create the directory to store the raw data if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save the combined data to a CSV file
    all_stats.to_csv("data/raw/player_game_logs.csv", index=False)
    print("Saved to data/raw/player_game_logs.csv")

# Run the function if the script is executed directly
if __name__ == "__main__":
    fetch_top_player_logs()