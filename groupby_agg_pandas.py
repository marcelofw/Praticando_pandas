import pandas as pd

df = pd.read_csv("dataset.csv")

#print(df[["Segmento", "Regiao", "Valor_Venda"]].groupby(["Segmento", "Regiao"]).mean())     #agrupar por valores não-numéricos
#aplica .mean() apenas para os valores numéricos

print(df[["Segmento", "Regiao", "Valor_Venda"]].groupby(["Segmento", "Regiao"]).agg(["mean", "std", "count"]))

