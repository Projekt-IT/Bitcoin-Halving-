import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv("BTC-USD.csv")
dataframe_sorted = dataframe.sort_values(["Date"], ascending=True)
dataframe_sorted_indexed = dataframe_sorted.set_index("Date")
print(dataframe_sorted_indexed)
dataframe_sorted_indexed.plot(figsize=(16,9))
plt.show()
testest