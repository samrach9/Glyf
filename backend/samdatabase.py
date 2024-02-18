import pandas as pd
import csv
from csv import writer
from fuzzysearch import find_near_matches_in_file
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

# print("old data:")
# data_ld = pd.read_csv('backend/data.csv')

# print(data_ld)
# print("\n")


# ADDING A NEW ROW 
# list that we want as a new row: schema of row: story, decade, event name, theme, location 
# new_row = ["We all sat down and wrote the Declaration of Independence, it was a lot of work", 1983, "Declaration of Independence", "Freedom", "USA", 1, "david"]

# # Open our existing CSV file in append mode and Create a file object for this file
# with open('backend/data.csv', 'a') as f_object:
#     # Pass this file object to csv.writer() and get a writer object
#     writer_object = writer(f_object)
 
#     # Pass the list as an argument into the writerow()
#     writer_object.writerow(new_row)
 
#     # Close the file object
#     f_object.close()

# print new data with new column
# Load the CSV file into a DataFrame
data_ld = pd.read_csv('backend/database.csv')
print(data_ld)
# Combine specific columns into a single string for fuzzy matching
data_ld['columns'] = data_ld['Summarized Story'] + ' ' + data_ld['Event Name'] + ' ' + data_ld['Theme'] + ' ' + data_ld['Location']

print(data_ld.dtypes)

# Prompt user for search query
searchstr = input("Enter your search: ")

# Define a function to perform fuzzy search across all columns
def fuzzy_search(query, choices, limit=2, scorer=fuzz.partial_ratio):
    results = process.extract(query, choices, limit=limit, scorer=scorer)
    return results

# Perform fuzzy search
choices = data_ld['columns']
results = fuzzy_search(searchstr, choices)

# Define the columns you want to display
columns_to_display = ['Original Story', 'Summarized Story', 'Decade', 'Event Name', 'Theme', 'Location']

# Print the selected columns for each match
for match in results:
    # match_index = match[2]  # Get the index of the matched row
    # matched_row = data_ld.iloc[match_index]  # Retrieve the row from the DataFrame
    # selected_columns = matched_row[columns_to_display]  # Select the specified columns
    print(match)

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