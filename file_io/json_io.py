import json

def read_json_file(filename):
    with open(filename, 'r') as data_file:
        data = json.loads(data_file.read())
        return data


def write_json_file(filename, data):
    with open(filename, 'w') as data_file:
        json.dump(data, data_file)
    print("\nDone! ")
    return data
