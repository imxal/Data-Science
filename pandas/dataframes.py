import pandas as pd

df = pd.DataFrame()
print(type(df))

df = pd.read_excel('PandasExample.xlsx')
print(df)

print(df.head())
print(df.tail())

print(df.head(2))
print(df.tail(2))

print(df.iloc[0])
print(df.values)

df = df[df['Age']>25]
print(df)