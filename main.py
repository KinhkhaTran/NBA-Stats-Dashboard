"""
main.py
-------
Orchestrates the full ETL → analysis → visualization pipeline for the
NBA 2024-25 Stats Dashboard.

Author  : Kinhkha Tran
Created : 2025-05-01
Project : NBA 2024-25 Stats Dashboard
Usage   : python main.py
Depends : scripts.fetch_data, scripts.process_data, scripts.visualize_data

Workflow
--------
1. Fetch raw player game logs via `nba_api` (fetch_data.py).
2. Clean and aggregate the logs into season averages (process_data.py).
3. Display a bar chart of the top scorers (visualize_data.py).

Notes
-----
• Each sub-module handles its own CLI args, but defaults make it
  safe to run this script with no parameters.
• Progress messages print to stdout; swap in `logging` for production.
• Expected project layout:
    project_root/
      ├─ scripts/
      │   ├─ fetch_data.py
      │   ├─ process_data.py
      │   └─ visualize_data.py
      └─ main.py
"""

# Import custom scripts for each part of the project pipeline
import scripts.fetch_data as fetch             # Handles data fetching from nba_api
import scripts.process_data as process         # Handles data cleaning and aggregation
import scripts.visualize_data as visualize     # Handles data visualization using matplotlib/seaborn

# Main function that runs the full workflow
def main():
    # Step 1: Fetch raw player game logs using nba_api
    print("Fetching NBA data...")
    fetch.fetch_top_player_logs()

    # Step 2: Process and clean the raw data, generate averages and new metrics
    print("Processing data...")
    process.process_stats()

    # Step 3: Plot the top scorers from the processed data
    print("Displaying top scorers...")
    visualize.plot_top_scorers()

# If this script is executed directly, run the main function
if __name__ == "__main__":
    main()