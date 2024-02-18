import pandas as pd
import csv
from csv import writer


# ORIGINAL DATA:
data_ld = pd.read_csv('backend/sethi_data_test.csv')
data_ld = data_ld.rename_axis('Submission Number')
print(data_ld)
print("\n")


# ADDING A NEW ROW 
# list that we want as a new row: schema of row: story, decade, event name, theme, location 
stry = "hahahaha"
new_row = [1983, "Declaration of Independence", "Freedom", "USA", 1, "david"]
new_row.insert(0, stry)

# Open our existing CSV file in append mode and Create a file object for this file
with open('backend/sethi_data_test.csv', 'a') as f_object:
    # Pass this file object to csv.writer() and get a writer object
    writer_object = writer(f_object)
 
    # Pass the list as an argument into the writerow()
    writer_object.writerow(new_row)
 
    # Close the file object
    f_object.close()

# print new data with new column
data_ld = pd.read_csv('backend/sethi_data_test.csv')
print(data_ld)

"""
# UPDATE LIKE COUNT, BY ROW NUMBER
row_number = 4
# save current like count 
current_like_count = data_ld["Likes"].loc[data_ld.index[row_number]]

# increment it
current_like_count = current_like_count + 1

#update like count
data_ld.at[row_number, "Likes"] = current_like_count


# update CSV file
data_ld._set_value(row_number, "Likes", current_like_count)
data_ld.to_csv("backend/sethi_data_test.csv", index=False)


# print new data with new cell
print(data_ld)
"""
