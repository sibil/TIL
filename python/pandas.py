import pandas as pd

brics = pd.read_csv("brics.csv", index_col = 0)

#iterating over a pandas dataframe - iterrows()

for label, row in brics.iterrows() :
  #Note that each row is a Panda Series, we can do row["country"] or row["another_column"]

# Add data to Panda Series - .loc[] or .iloc[]
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
 
Another way it to use .apply()
This is the preferred option. 
cars["COUNTRY"] = cars["country"].apply(str.upper)
or
cars["COUNTRYLEN"] = cars["country"].apply(len)
