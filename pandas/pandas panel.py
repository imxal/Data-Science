import pandas as pd
df = pd.read_excel("PandasExample.xlsx")
print(df.head)
print(df.set_index(['Gender']))
print(df.index)

