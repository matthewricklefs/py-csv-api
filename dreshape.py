import numpy as np
import pandas as pd

# read existing csv from fetch request
df = pd.read_csv('ucla-long.csv')
print('-'*100)
print('OG DF: ')
print(df.head())
print('-'*100)

# spread years horizontally / display population value for each year
# pivotFrame = pd.pivot_table(df, index='State Name', columns='Year', aggfunc='sum', values="Population", margins='Population', margins_name=f"2019 Factors")
pivotFrame = pd.pivot(df, index='State Name', columns='Year', values="Population")
print('-'*100)
print('PIVOTED DF: ')
print(pivotFrame)
print('-'*100)

def unpivot(frame):
    N, K = frame.shape
    data = {
        "value": frame.to_numpy().ravel("F"),
        "variable": np.asarray(frame.columns).repeat(N),
        "date": np.tile(np.asarray(frame.index), K),
    }
    return pd.DataFrame(data, columns=["date", "variable", "value"])

# newdata = []
# def percentChange(first, second):
#     return (second - first) / first  * 100.00

# print('-'*100)
# print(df['Population'])
# print('-'*100)
# pct_change = percentChange(df['Population'])

# for x in df:
#     pct_change = percentChange(x, (x+1))
#     listing = [x['State'], x['Year'], x[f'Population ({pct_change})']] 
#     newdata.append(listing)

# kinda got something good back

# convert population growth/decrease into percentage value
# percentChange = pd.pivot_table(df, index="State Name", columns='Year', aggfunc='sum', values='Population').pct_change()
# print('-'*100)
# print('PERCENT CHANGE DF: ')
# print(percentChange)
# print('-'*100)


# spread years horizontally / display population value for each year
# df2 = percentChange.pivot(df, index='State Name', columns='Year', values=["Population"])
# print('-'*100)
# print('VALUE COUNT: ')
# pop_percent = pd.concat([pivotFrame, percentChange], axis='columns', sort=False)
# print(pop_percent)
# print('-'*100)

# -------
# so i would create a function to baskially do your percentage calc


# def addChangeToCSV(indexStart, indexEnd):
#     for(i = indexStart; i <= indexEndPoint; i++):

# export to csv
# df2.to_csv('ucla-data.csv')
