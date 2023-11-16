import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

db_config = {
    'host': 'localhost',
    'user': 'lscloud',
    'password': 'lscloud',
    'database': 'lscloud'
}

try:
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()
    cursor.execute("SELECT chlorine_residual FROM well_readings WHERE well_id = 29")
    rows = cursor.fetchall()

    data_list = [float(item[0]) for item in rows]

    # Create a pandas Series
    series = pd.Series(data_list)

    # Calculate basic descriptive statistics
    mean_value = series.mean()
    median_value = series.median()
    mode_value = series.mode().values[0]

    # Create a histogram
    plt.hist(data_list, bins='auto', alpha=0.7, color='blue', edgecolor='black')
    plt.title('Barbour Point Well Residual')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

    # Print descriptive statistics
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Mode:", mode_value)
    print("Standard Deviation:", series.std())
    print("Skewness:", series.skew())
    print("Kurtosis:", series.kurtosis())

except mysql.connector.Error as error:
    print("Failed to get record from MySQL table: {}".format(error))




