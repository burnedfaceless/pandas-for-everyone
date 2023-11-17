import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


def calculate_gallons_per_day(df):
    # Sort the DataFrame by date
    df.sort_values(by='date_of_reading', inplace=True)

    # Calculate the time difference between consecutive readings
    df['days_diff'] = (df['date_of_reading'] - df['date_of_reading'].shift()).dt.days.fillna(0)

    # Calculate gallons pumped per day
    df['gallons_per_day'] = df['pump'] / df['days_diff'].replace(0, 1)

    # Drop unnecessary columns
    df.drop(columns=['days_diff'], inplace=True)

    return df


def main():
    # Database connection configuration
    db_config = {
        'host': 'localhost',
        'user': 'lscloud',
        'password': 'lscloud',
        'database': 'lscloud'
    }

    # Well ID for which pump readings need to be retrieved
    well_id_to_query = 43  # Replace with the desired well ID

    try:
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)

        # Retrieve the most recent 30 pump readings for the specified well ID
        query = f"SELECT pump, date_of_reading FROM well_readings WHERE well_id = {well_id_to_query} ORDER BY date_of_reading DESC LIMIT 30"
        df = pd.read_sql(query, connection)

        # Calculate gallons pumped per day
        df = calculate_gallons_per_day(df)

        # Display the resulting DataFrame
        print(df)

        # Create a histogram
        plt.hist(df['gallons_per_day'], bins='auto', alpha=0.7, color='blue', edgecolor='black')
        plt.title('Gallons Pumped Per Last 30 Days Histogram')
        plt.xlabel('Gallons Per Day')
        plt.ylabel('Frequency')
        plt.show()

        # Print descriptive statistics
        print("Mean:", df['gallons_per_day'].mean())
        print("Median:", df['gallons_per_day'].median())
        print("Mode:", df['gallons_per_day'].mode().values[0])
        print("Standard Deviation:", df['gallons_per_day'].std())
        print("Skewness:", df['gallons_per_day'].skew())
        print("Kurtosis:", df['gallons_per_day'].kurtosis())

    except mysql.connector.Error as error:
        print("Failed to get records from MySQL table: {}".format(error))
    finally:
        # Close the database connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    main()