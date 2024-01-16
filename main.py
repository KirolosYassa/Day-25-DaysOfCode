filename = "./weather_data.csv"
with open(filename, 'r') as file:
    content_list = file.readlines()
    
print(content_list)