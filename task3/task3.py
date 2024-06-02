import json
import sys

def load_json(file_path):
  with open(file_path, 'r') as file:
    return json.load(file)

def save_json(data, file_path):
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

def fill_values(data, value_dict):
  if isinstance(data, dict):
    if 'id' in data and data['id'] in value_dict:
      data['value'] = value_dict[data['id']]
    for key in data:
      if isinstance(data[key], (dict, list)):
        fill_values(data[key], value_dict)
  elif isinstance(data, list):
    for item in data:
      fill_values(item, value_dict)

def main(args):
  if len(args) != 3: return print("Expected 3 args")
  values = load_json(args[0])
  tests = load_json(args[1])
  value_dict = {item['id']: item['value'] for item in values}
  fill_values(tests, value_dict)
  save_json(tests, args[2])

if __name__ == "__main__":
  main(sys.argv[1:])
