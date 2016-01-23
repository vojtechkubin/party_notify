from person import Person_encoder
import json


def save(data, file_name = 'database'):

    tmp = {}

    print(data)

    for item in data:
        
        tmp[item] = Person_encoder().encode(data[item])

    print(tmp)

    file_name = file_extension(file_name)
    with open(file_name, 'w') as data_file:
        data_file.write(json.dumps(tmp, sort_keys = True, indent = 4))

def load(file_name = 'database'):
    file_name = file_extension(file_name)
    with open(file_name) as data_file:
        data = json.load(data_file)
    return data

def file_extension(file_name):
    result = file_name.strip()
    if '.json' not in result:
        result += '.json'
    return result
