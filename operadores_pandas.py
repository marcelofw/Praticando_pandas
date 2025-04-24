import pandas as pd

df = pd.read_csv("dataset.csv")
#print(df.head())

#print(df[(df.Segmento == "Home Office") & (df.Regiao == "South")].head())      #and

#print(df [(df.Segmento == "Home Office") | (df.Regiao == "South")].tail())      #pipe = or

print(df [(df.Segmento != "Home Office") & (df.Regiao != "South")].sample(5))

