import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PandasExample.xlsx')
df.sort_index(inplace=True)
print(df.head())
plt.plot(df['Age'])
plt.show()

plt.boxplot(df['Age'])
plt.show()

plt.hist(df['Age'])
plt.show()

plt.xlabel('Age')
plt.ylabel('Id')
plt.title('Scatter Plot')
plt.scatter(x=df['Age'],y=df['ID'])
plt.show()

d={'a':10, 'b':20, 'c':13}
plt.bar(x=d.keys(),height=d.values())
plt.show()

plt.pie(x=d.keys(),height=d.values())
plt.show()



#3d plotting

df['H-L'] = df.High - df.Low
df['10MA']=df['Age'].rolling(10).mean()

ax=plt.axes(projection='3d')
ax.scatter(df.index, df['H-L'], df['10MA'])
ax.set_xlabel('Index')
ax.set_ylabel('H-L')
ax.set_zlabel('10MA')
plt.show()