import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("breadprice.csv")

data["Average"] = data.loc[:, "Jan":"Dec"].mean(axis=1)

print(data[["Year", "Average"]])

plt.plot(data["Year"], data["Average"], marker='o', color='orange')
plt.title("Average Bread Prices Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Price")
plt.grid(True)
plt.tight_layout()
plt.show()
