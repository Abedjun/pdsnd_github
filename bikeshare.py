import pandas as pd

# Sample bike share data
DATA = {
    'Start Time': ['2022-01-01 00:05', '2022-01-01 00:15', '2022-01-01 00:30'],
    'End Time': ['2022-01-01 00:25', '2022-01-01 00:35', '2022-01-01 00:50'],
    'Trip Duration': [20, 20, 20],
    'Start Station': ['Station A', 'Station B', 'Station A'],
    'End Station': ['Station B', 'Station C', 'Station B'],
}

# Convert data to DataFrame
dff = pd.DataFrame(DATA)

# Function to load data from a CSV file
def load_data(filename):
    """
    Loads the bike-sharing data from a CSV file.
    
    Args:
        filename (str): The path to the CSV file.
    
    Returns:
        DataFrame: A pandas DataFrame containing the data.
    """
    return pd.read_csv(filename)

# Function to calculate total trip duration
def total_trip_duration():
    total_duration = dff['Trip Duration'].sum()
    print(f"Total Trip Duration: {total_duration} minutes")

# Function to find the most frequent start station
def most_frequent_start_station():
    frequent_station = dff['Start Station'].mode()[0]
    print(f"Most Frequent Start Station: {frequent_station}")

if __name__ == "__main__":
    total_trip_duration()
    most_frequent_start_station()
