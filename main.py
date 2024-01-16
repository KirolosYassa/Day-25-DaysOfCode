# filename = "./weather_data.csv"
# with open(filename, 'r') as file:
#     content_list = file.readlines()
    
# print(content_list)

import csv

filename = "./weather_data.csv"
with open(filename, 'r') as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        print(row)
