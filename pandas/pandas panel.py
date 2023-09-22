import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("PandasExample.xlsx")
print(df.head)
print(df.set_index(['Gender']))
print(df.index)

print(df.columns)
print(df.plot())
plt.show()

print(df['Age'].plot(kind='hist', title='Histogram'))
plt.show()