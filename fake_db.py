import json
import pickle


def save(data, file_name = 'database'):
    filen = file_extension(file_name)

    with open(filen,"wb") as pickle_out:
        pickle.dump(data, pickle_out)

def load(file_name = 'database'):
    filen = file_extension(file_name)

    with open(filen, "rb") as pickle_in: 
        data = pickle.load(pickle_in)
 
    return data

def file_extension(file_name):
    result = file_name.strip()
    if '.json' not in result:
        result += '.json'
    return result

