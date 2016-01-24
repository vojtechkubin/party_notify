import json
import person
import pickle


def save(data, file_name = 'database'):
    filen = file_extension(file_name)
    pickle_out = open(filen,"wb")

    pickle.dump(data, pickle_out)

    pickle_out.close()

def load(file_name = 'database'):
    filen = file_extension(file_name)
    pickle_in = open(filen, "rb")
    data = pickle.load(pickle_in)
    pickle_in.close()
    return data

def file_extension(file_name):
    result = file_name.strip()
    if '.json' not in result:
        result += '.json'
    return result

