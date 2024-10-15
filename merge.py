import json
import os

input_dir = 'data/peoples/'
output_file = 'data/peoples.json'
json_files = ['blueskychan.json', 'bluestar.json', 'furrygang.json']
merged_data = []

for json_file in json_files:
    file_path = os.path.join(input_dir, json_file)
    with open(file_path, 'r') as f:
        data = json.load(f)
        merged_data.append(data)

with open(output_file, 'w') as f:
    json.dump(merged_data, f, indent=4)

print(f'Merged data written to {output_file}')
