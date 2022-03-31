import pandas as pd

# read existing csv from fetch request
df = pd.read_csv('ucla-long.csv')
print('-'*100)
print('OG DF: ')
print(df.head())
print('-'*100)

# spread years horizontally / display population value for each year
# pivotFrame = pd.pivot_table(df, index='State Name', columns='Year', aggfunc='sum', values="Population", margins='Population', margins_name=f"2019 Factors")
pivotFrame = pd.pivot_table(df, index='State Name', columns='Year', aggfunc='sum', values="Population")
print('-'*100)
print('PIVOTED DF: ')
print(pivotFrame)
print('-'*100)

# convert population growth/decrease into percentage value
percentChange = pd.pivot_table(df, index="State Name", columns='Year', aggfunc='sum', values='Population').pct_change()
print('-'*100)
print('PERCENT CHANGE DF: ')
print(percentChange)
print('-'*100)

# spread years horizontally / display population value for each year
# df2 = percentChange.pivot(df, index='State Name', columns='Year', values=["Population"])
print('-'*100)
print('VALUE COUNT: ')
pop_percent = pd.concat([pivotFrame, percentChange], axis='columns', sort=False)
print(pop_percent)
print('-'*100)

# -------

# export to csv
# df2.to_csv('ucla-data.csv')
