import json
import os

input_dir = 'data/peoples/'
output_file = 'data/peoples.json'
json_files = ['blueskychan_.json', 'bluestar.json', 'furrygang.json', 'mizuki403_.json']
merged_data = []

for json_file in json_files:
    print(json_file)
    file_path = os.path.join(input_dir, json_file)
    with open(file_path, 'r') as f:
        data = json.load(f)
        merged_data.append(data)

with open(output_file, 'w') as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)

print(f'Merged data written to {output_file}')
