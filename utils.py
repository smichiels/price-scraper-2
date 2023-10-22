import json

from collections import namedtuple

ComponentTuple = namedtuple('ComponentTuple', ['name', 'store', 'price'])


def read_json_file(filename):
    with open(filename, 'r') as data_file:
        data = json.loads(data_file.read())
        return data


def write_json_file(filename, data):
    with open(filename, 'w') as data_file:
        json.dump(data, fp=data_file, indent=2)
    print("\nDone! ")
    return data


def get_minimum_build(obj_list):
    final_component_list = [get_min_store(obj) for obj in obj_list]
    total = 0
    for comp in final_component_list:
        print(f"Buy {comp.name} in {comp.store.replace('_price', '')} - {comp.price}€")
        total = total + comp.price
    print(f"Total: {'%.2f' %total}€")


def get_min_store(obj):
    aux_dict = {}
    for (key, value) in obj["prices"].items():
        if 'last' not in key and value is not None:
            aux_dict[key] = value
    store = min(aux_dict, key=aux_dict.get)
    return ComponentTuple(obj["name"], store, aux_dict[store])
