import json
import os

input_dir = 'data/peoples/'
output_file = 'data/peoples.json'

json_files = {'blueskychan_.json', 'bluestar.json', 'furrygang.json', 'mizuki403_.json', 'nyarutoru.json', 'danielrockford.json'}

allowed_schema = {
    "name": (str, type(None)),
    "irl_name": (str, type(None)),
    "desc": (str, type(None)),
    "birth_date": (str, type(None)),
    "role": (str, type(None)),
    "pronouns": (str, type(None)),
    "link": (str, type(None)),
    "contacts": list
}

merged_data = []

actual_files = set(os.listdir(input_dir))

for json_file in actual_files:
    file_path = os.path.join(input_dir, json_file)

    if json_file not in json_files:
        print(f'Warning: {json_file} exists but is not allowed to merge due to not being in the list.')
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, dict):
            print(f'Error: {json_file} is not a valid JSON object and will be skipped. [Schema Detection: Failed]')
            continue

        if set(data.keys()) != set(allowed_schema.keys()):
            print(f'Error: {json_file} has missing or extra keys and will be skipped. [Schema Detection: Failed]')
            continue

        if not all(isinstance(data[key], allowed_schema[key]) for key in allowed_schema):
            print(f'Error: {json_file} contains invalid value types and will be skipped. [Schema Detection: Failed]')
            continue

        if not isinstance(data["contacts"], list):
            print(f'Error: {json_file} has an invalid contacts format and will be skipped. [Schema Detection: Failed]')
            continue

        for contact in data["contacts"]:
            if not isinstance(contact, dict):
                print(f'Error: {json_file} has an invalid contacts format and will be skipped. [Schema Detection: Failed]')
                continue

            if not any(isinstance(value, str) for value in contact.values()):
                print(f'Error: {json_file} has an invalid contacts format and will be skipped. [Schema Detection: Failed]')
                continue

        print(f'Success: {json_file} passed schema validation. [Schema Detection: Passed]')
        merged_data.append(data)

    except json.JSONDecodeError:
        print(f'Error: {json_file} contains invalid JSON and will be skipped. [Schema Detection: Failed]')

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)

print(f'Merged data written to {output_file}')
