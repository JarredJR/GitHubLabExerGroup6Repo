import requests
import matplotlib.pyplot as plt

url = "https://disease.sh/v3/covid-19/historical/Philippines?lastdays=30"
response = requests.get(url)
data = response.json()

cases = data["timeline"]["cases"]
dates = list(cases.keys())
values = list(cases.values())

plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker="o", color="blue")
plt.title("COVID-19 Cases in the Philippines (Last 30 Days)")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
