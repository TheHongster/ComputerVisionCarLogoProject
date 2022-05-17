import json

file = open('results_JSON.json')
data = json.load(file)

#data[0]['objects'][0]['relative_coordinates']['center_x']
print(data[1]['objects'][0]['relative_coordinates']['center_x'])