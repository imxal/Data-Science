import pandas as pd

l = [x for x in range(5)]
s=pd.Series(l)
print(s)
print(s[3])


s = pd.Series(l, index=['a','b','c','d','e'])
print(s)
print(s['e'])

s = pd.Series(l, index=['a','b','c','d','d'])
print(s['d'])

data = {'f':6,'g':7,'h':8,'i':9,'j':10}
s = pd.Series(data)
print(s)


a = pd.Series([x for x in range(1,11)])
print(a)

print(a.iloc[0])
print(a.iloc[5])
print(a.iat[8])
print(a[4:9])

print(a.where(a%2==0, 'Odd number'))
print(a.where(a%2==0, a**2))
a.where(a%2==0, inplace=True)
print(a.dropna())
print(a.fillna("filled value"))






