import pandas as pd


# read existing csv from fetch request
df = pd.read_csv('ucla-long.csv')
print(df)

# spread years horizontally / display population value for each year
percentChange = pd.pivot_table(df, index='State Name', columns='Year', aggfunc='sum', values="Population")
print(percentChange)

# convert population growth/decrease into percentage value
print(percentChange.pct_change())





# spread years horizontally / display population value for each year
# df2 = df.pivot(index='State Name', columns='Year', values="Population")
# print(df2)

# export to csv
# df2.to_csv('ucla-data.csv')

# convert 
# new_df = df.groupby('Year')['Population'].value_counts(normalize=True)
# new_df = new_df.mul(100).rename('Percent')
# print(new_df)