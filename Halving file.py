import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv("BTC-USD.csv")
dataframe_sorted = dataframe.sort_values(["Date"], ascending=True)
dataframe_sorted_indexed = dataframe_sorted.set_index("Date")
print(dataframe_sorted_indexed)
dataframe_sorted_indexed.plot(figsize=(16,9))

#Überschrift
plt.title("BTC-Aktie - Halvings")

#Schwarzer Hintergrund
plt.style.use("dark_background")

#Achsenbeschriftung
plt.xlabel("Date")
plt.ylabel("Close Stock Value")

#Gitternetz einfügen
plt.grid()

plt.show()