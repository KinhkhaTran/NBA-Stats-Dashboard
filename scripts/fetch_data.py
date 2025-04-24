from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd
import time
import os

def fetch_top_player_logs(limit=30, season='2024-25'):
    all_players = players.get_active_players()
    player_stats = []

    for player in all_players[:limit]:
        try:
            logs = playergamelog.PlayerGameLog(
                player_id=player['id'],
                season=season,
                season_type_all_star='Regular Season'
            )
            df = logs.get_data_frames()[0]
            df['Player'] = player['full_name']
            player_stats.append(df)
            print(f"Fetched data for {player['full_name']}")
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching {player['full_name']}: {e}")

    all_stats = pd.concat(player_stats)
    os.makedirs("data/raw", exist_ok=True)
    all_stats.to_csv("data/raw/player_game_logs.csv", index=False)
    print("Saved to data/raw/player_game_logs.csv")

if __name__ == "__main__":
    fetch_top_player_logs()