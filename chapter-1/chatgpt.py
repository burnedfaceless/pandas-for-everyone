import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a pandas Series
series = pd.Series(data)

# Calculate basic descriptive statistics
mean_value = series.mean()
median_value = series.median()
mode_value = series.mode().values[0]

# Create a histogram
plt.hist(data, bins='auto', alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Data')
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