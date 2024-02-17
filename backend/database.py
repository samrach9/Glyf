import pandas as pd
import csv
from csv import writer

print("old data:")
data_ld = pd.read_csv('/Users/anikasethi/Documents/GitHub/Glyf/backend/data.csv')

print(data_ld)
print("\n")


# ADDING A NEW ROW 
# list that we want as a new row: schema of row: story, decade, event name, theme, location 
new_row = ["We all sat down and wrote the Declaration of Independence, it was a lot of work", 1983, "Declaration of Independence", "Freedom", "USA", 1, "david"]

# Open our existing CSV file in append mode and Create a file object for this file
with open('/Users/anikasethi/Documents/GitHub/Glyf/backend/data.csv', 'a') as f_object:
    # Pass this file object to csv.writer() and get a writer object
    writer_object = writer(f_object)
 
    # Pass the list as an argument into the writerow()
    writer_object.writerow(new_row)
 
    # Close the file object
    f_object.close()

# print new data with new column
data_ld = pd.read_csv('/Users/anikasethi/Documents/GitHub/Glyf/backend/data.csv')
print(data_ld)

"""

# UPDATE ONE CALL (LIKE COUNT)
# reading the csv file 
df = pd.read_csv("/Users/anikasethi/Documents/GitHub/Glyf/backend/data.csv") 
  
# updating the column value/data 
df.loc[5, 'likes'] = 'SHIV CHANDRA'
  
# writing into the file 
df.to_csv("/Users/anikasethi/Documents/GitHub/Glyf/backend/data.csv", index=False) 
  
print(df) 
"""


"""
a = {}

a['id'] = {1, 2}
a['decade'] = {1940, 1776}
a['event name'] = {"Partition", "Declaration of Independence"}
a['location'] = {'India/Pakistan', "USA"}
a['theme'] = {'Saddness', 'Freedom'}

print(a)
"""

