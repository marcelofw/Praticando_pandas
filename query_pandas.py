import pandas as pd

df = pd.read_csv("dataset.csv")
# print(df.head())

moda = df["Quantidade"].value_counts().index[0]
df["Quantidade"].fillna(value = moda, inplace = True)

#print(df.Valor_Venda.describe())
df2 = df.query("229 < Valor_Venda < 10000")
#print(df2.Valor_Venda.describe())

df3 = df2.query("Valor_Venda > 766")
#print(df3.head())


