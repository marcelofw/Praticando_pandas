import pandas as pd
from pandas import DataFrame
import numpy as np

dados = {"Cidade": ["Thais", "Venore", "Liberty Bay", "Carlin", "Port Hope"],
         "Ano": [2012, 2013, 2014, 2015, 2016],
         "Taxa Desemprego": [1.5, 1.7, 1.6, 2.4, 2.7]}

# df = DataFrame(dados)
# print(df)
# print(type(df))
# print(df.head())

# print(DataFrame(dados, columns = ["Cidade", "Taxa Desemprego", "Ano"]))

df2 = DataFrame(dados, 
                columns = ["Cidade", "Taxa Desemprego", "Taxa Crescimento", "Ano"], 
                index = ["cidade1", "cidade2", "cidade3", "cidade4", "cidade5"])
# print(df2)
# print(df2.values)
# print(df2.columns)
# print(df2["Cidade"])
# print(df2[["Taxa Desemprego", "Ano"]])
# print(df2.index)
# print(df2.filter(items = ["cidade3"], axis = 0))
# print(df2.head())
# print(df2.describe())
# print(df2.isna())
# print(df2["Taxa Crescimento"].isna())

# df2["Taxa Crescimento"] = np.arange(5.)
# print(df2)
# print(df2["Taxa Crescimento"].isna())
# print(df2.describe())

# print(df2["cidade2":"cidade4"])
# print(df2[df2["Taxa Desemprego"] < 2])

# print(df2[["Cidade", "Taxa Crescimento"]])
# print(df2[["Cidade", "Taxa Crescimento", "Ano"]])
