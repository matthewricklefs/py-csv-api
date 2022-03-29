import pandas as pd


df = pd.read_csv('crypto.csv', encoding='unicode_escape')
print(df)

df2 = df.pivot(index='')