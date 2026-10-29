import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Homework 20/sales_clean.csv")
df = df.groupby("seller")["total"].sum().sort_values(ascending=False)

df.to_csv("Homework 20/sellers.csv", index=False)
df.plot(kind="bar", title="Дохід за продавцями", rot=0)
plt.tight_layout()
plt.savefig("Homework 20/sellers.png")