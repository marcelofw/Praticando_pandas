import pandas as pd

df = pd.read_csv("dataset.csv")
#print(df.head(5))
#print(df.isna().sum())

moda = df["Quantidade"].value_counts().index[0]
#print(moda)
df["Quantidade"].fillna(value = moda, inplace = True)
print(df.isna().sum())
