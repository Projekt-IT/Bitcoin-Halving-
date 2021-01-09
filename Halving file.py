import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataframe = pd.read_csv("BTC-USD.csv")

dataframe_sorted = dataframe.sort_values(["Date"], ascending=True)
dataframe_sorted_indexed = dataframe_sorted.set_index("Date")
print(dataframe_sorted_indexed)
dataframe_sorted_indexed.plot(figsize=(16,9))

#Schwarzer Hintergrund
plt.style.use("dark_background")
#-> funktioniert nicht

#Überschrift
plt.title("BTC-Aktie - Halvings")

#Achsenbeschriftung
plt.xlabel("Date")
plt.ylabel("Close Stock Value")

#Gitternetz einfügen
plt.grid()

#Skalierung absolut y-Achse
plt.ylim(0, 25000)

#Skalierung Abstufung y-Achse
plt.yticks(np.arange(0, 25000, 1000))

#Skalierung x-Achse


#Vertikale  Linie an der Stelle 'x_pos' für Halvings
#x_pos = 2016-01-03
plt.vlines(x = 2016, color = "c", ymin = 0, ymax = 25000)
#-> position in datetime bekommen

plt.show()