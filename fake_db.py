import json


def save(data, file_name = 'database'):

    tmp = {}

    for item in data:
        tmp[item] = Encoder(indent = 4).encode(data[item])

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

class Encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

