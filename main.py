import scripts.fetch_data as fetch
import scripts.process_data as process
import scripts.visualize_data as visualize

def main():
    print("Fetching NBA data...")
    fetch.fetch_top_player_logs()

    print("Processing data...")
    process.process_stats()

    print("Displaying top scorers...")
    visualize.plot_top_scorers()

if __name__ == "__main__":
    main()