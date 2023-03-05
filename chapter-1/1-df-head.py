import pandas as pd

# by default, read_csv() assumes that the separator is a comma
# if you want to use a tab, you need to specify it
df = pd.read_csv('gapminder.tsv', sep='\t')

# Print the head of the DataFrame
print(df.head())
