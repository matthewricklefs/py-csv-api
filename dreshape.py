import pandas as pd



df = pd.read_csv('crypto.csv', encoding='unicode_escape')
print(df)

df2 = df.pivot(index='State Name', columns='Year', values="Population")
print(df2)

df2.to_csv('ucla-data.csv')