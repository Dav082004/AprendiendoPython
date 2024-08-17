import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("prom_graf\\datosfechas.csv")

sns.lineplot(x="fecha", y="cantidad",data=df)

plt.plot("01-05",8,"o")

plt.show()
