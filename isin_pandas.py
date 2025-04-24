import pandas as pd

df = pd.read_csv("dataset.csv")
# print(df.shape)     #(linhas, colunas)

filtro = df[df["Quantidade"].isin([5, 7, 9, 11])]
# print(filtro)
print(filtro.shape)

print(filtro[:10])
