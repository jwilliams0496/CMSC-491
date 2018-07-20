import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("http://stats.idre.ucla.edu/stat/data/binary.csv", skipinitialspace=True)
print data.head()

data.mean()
data.std()
data.std().index
data.std().values

print "butts"

counts = data["gre"].value_counts()
bucket = 1

print "poop"

iCounts = counts.sort_index()
iCounts.plot(kind = 'bar')
plt.show()
