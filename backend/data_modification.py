import pandas as pd
import csv
from csv import writer
from openai_test import story
from openai_test import attributes

"""
# This file contains functions to modify the DATABASE.CSV file
# Possible modifications include: 
# 1) Adding a new Story + all of the tags that go with it 
# 2) Updating the like count of a story given it's Submission Number
"""
def NewStory(new_row):     # new_row is a list of strings with the values for the columns in order
    new_row.append(0)      # Add like count to end of database (default for new story is 0)

    # Open our existing CSV file in append mode and Create a file object for this file
    with open('backend/database.csv', 'a') as f_object:
        # Pass this file object to csv.writer() and get a writer object
        writer_object = writer(f_object)
        # Pass the list as an argument into the writerow()
        writer_object.writerow(new_row)
        # Close the file object
        f_object.close()

    data_ld = pd.read_csv('backend/database.csv')
    data_ld = data_ld.rename_axis('Submission Number')
    # TESTING: print new data with new column
    # print(data_ld)

def UpdateLikeCount(row_number):
    data_ld = pd.read_csv('backend/database.csv')
    data_ld = data_ld.rename_axis('Submission Number')

    # save current like count 
    current_like_count = data_ld["Likes"].loc[data_ld.index[row_number]]

    # increment it
    current_like_count = current_like_count + 1

    #update like count
    data_ld.at[row_number, "Likes"] = current_like_count

    # update CSV file
    data_ld._set_value(row_number, "Likes", current_like_count)
    data_ld.to_csv("backend/database.csv", index=False)

    # TESTING: print new data with new cell
    # print(data_ld)



# Testing
# new_data = ["Jack and Jill went up the hill To fetch a pail of water; Jack fell down and broke his crown, And Jill came tumbling after.", "JACK AND JILL FELL", 1777, "Hike", "Death", "The Netherlands"]
# print(type(new_data))

# NewStory(new_data)
# UpdateLikeCount(0)
    

