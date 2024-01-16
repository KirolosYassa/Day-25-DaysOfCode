# filename = "./weather_data.csv"
# with open(filename, 'r') as file:
#     content_list = file.readlines()
    
# print(content_list)

# import csv

# filename = "./weather_data.csv"
# with open(filename, 'r') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         # print(row)
#         temperature.append(row[1])
        
# print(temperature[1,])

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])
