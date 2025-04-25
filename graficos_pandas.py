import sklearn
#print(sklearn.__version__)
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
data = load_iris()

df = pd.DataFrame(data["data"], columns = data["feature_names"])
df["species"] = data["target"]
#print(df.head())

# df.plot()
# plt.show()

# df.plot.scatter(x = "sepal length (cm)", y = "sepal width (cm)")
# plt.show()

# columns = ["sepal length (cm)", "petal length (cm)", "petal width (cm)", "sepal width (cm)"]
# df[columns].plot.area()
# plt.show()













