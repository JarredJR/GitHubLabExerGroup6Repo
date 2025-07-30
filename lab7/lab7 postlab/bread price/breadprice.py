import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("breadprice.csv")

data_clean = data.dropna()

data_clean['Average Price'] = data_clean.iloc[:, 1:].mean(axis=1)

plt.figure(figsize=(10, 5))
plt.plot(data_clean["Year"], data_clean["Average Price"], marker='o', linestyle='-', color='orange')
plt.title("Average Bread Price per Year")
plt.xlabel("Year")
plt.ylabel("Average Price ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("bread_price_plot.png") 
plt.show()
