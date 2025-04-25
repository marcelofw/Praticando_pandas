import pandas as pd

df = pd.read_csv("dataset.csv")
# print(df[df.Segmento.str.startswith("Con")].head())
# print(df[df.Segmento.str.endswith("mer")].head())

# print(df["ID_Pedido"].head())

#print(df["ID_Pedido"].str.split("-"))      

#print(df["ID_Pedido"].str.split("-").str[1].head())

# df["Ano"] = df["ID_Pedido"].str.split("-").str[1]       
# print(df.head())

# print(df.head(3))
# print(df["Data_Pedido"].head(3))
# print(df["Data_Pedido"].str.lstrip("20"))

# df["ID_Cliente"] = df["ID_Cliente"].str.replace("CG", "AX")
# print(df.head())

#print(df.head())
df["Pedido_Segmento"] = df["ID_Pedido"].str.cat(df["Segmento"], sep = "-")
print(df.head())
