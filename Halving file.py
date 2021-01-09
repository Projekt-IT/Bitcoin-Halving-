import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataframe = pd.read_csv("BTC-USD.csv")

#nur Closing Stock Value anzeigen
extr_dataframe = dataframe[["Date","Adj Close"]]
print(extr_dataframe)

#nach Datum sortieren
extr_dataframe_sorted = extr_dataframe.sort_values(["Date"], ascending=True)
extr_dataframe_sorted_indexed = extr_dataframe_sorted.set_index("Date")
print(extr_dataframe_sorted_indexed)

#Graph einführen
extr_dataframe_sorted_indexed.plot(figsize=(16,9))

#Schwarzer Hintergrund
plt.style.use("dark_background")
#-> funktioniert nicht

#Überschrift
plt.title("BTC-Aktie - Halvings")

#Achsenbeschriftung
plt.xlabel("Date")
plt.ylabel("Closing Stock Value")

#Gitternetz einfügen
plt.grid()

#Skalierung absolut y-Achse
plt.ylim(0, 25000)

#Skalierung Abstufung y-Achse
plt.yticks(np.arange(0, 25000, 1000))

#dateformat in monat/Jahr (mit DateFormatter), Eingabeformate (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#date_format = DateFormatter("%b-%y")

#Skalierung x-Achse (in Datetime umwandeln)


#Vertikale  Linie an der Stelle 'x_pos' für Halvings
plt.vlines(x = 2, color = "c", ymin = 0, ymax = 25000)
#-> position in datetime bekommen

plt.show()