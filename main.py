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