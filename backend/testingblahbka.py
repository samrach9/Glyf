
import csv
import json
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments

def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to be the primary key
            key = rows["Original Story"]
            data[key] = rows
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    """with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))"""

    json_obj = json.dumps(data, indent=4)
    return (json_obj)

         
# Testing
# Decide the two file paths according to your 
# computer system
csvFilePath = r'/Users/anikasethi/Documents/GitHub/Glyf/backend/sethi_test_database.csv'
jsonFilePath = r'/Users/anikasethi/Documents/GitHub/Glyf/frontend/testbla.json'
 

print(type(jsonFilePath))
# Call the make_json function

print(make_json(csvFilePath, jsonFilePath))

