import pandas as pd

df = pd.read_csv("dataset.csv")
# print(df[df.Segmento.str.startswith("Con")].head())
# print(df[df.Segmento.str.endswith("mer")].head())

# print(df["ID_Pedido"].head())

#print(df["ID_Pedido"].str.split("-"))      

#print(df["ID_Pedido"].str.split("-").str[1].head())

df["Ano"] = df["ID_Pedido"].str.split("-").str[1]       
print(df.head())



















