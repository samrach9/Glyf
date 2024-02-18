import csv
import json

def make_json(csvFilePath, jsonFilePath):
    # create a list to hold the data
    data = []
    
    # Open the CSV file and read its contents
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Iterate over each row in the CSV file
        for idx, rows in enumerate(csvReader):
            # Add the row data to the list with the row number as the key
            data.append({idx: rows})
            
    # Write the list of dictionaries to a JSON file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4)
 

         
# Testing
# Decide the two file paths according to your 
# computer system
csvFilePath = r'/Users/anikasethi/Documents/GitHub/Glyf/backend/sethi_test_database.csv'
jsonFilePath = r'/Users/anikasethi/Documents/GitHub/Glyf/frontend/testbla.json'
 

print(type(jsonFilePath))
# Call the make_json function

hi = make_json(csvFilePath, jsonFilePath)
print(type(hi))

