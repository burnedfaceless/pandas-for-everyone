import pandas as pd

# by default, read_csv() assumes that the separator is a comma
# if you want to use a tab, you need to specify it
df = pd.read_csv('gapminder.tsv', sep='\t')

# just get the country column and save it as a new variable
country_df = df['country']

# show the first 5 observations
print(country_df.head())

# show the last 5 observations
print(country_df.tail())
