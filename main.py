import yaml
import json

with open("timetable.json", 'r', encoding='utf-8') as input:
    json_object = json.load(input)
    print(yaml.dump(json_object))






