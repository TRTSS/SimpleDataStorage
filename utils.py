import os
import json
from pydoc import locate

import main


class Document:
    def __init__(self, abs_path: str):
        data = json.loads(open(abs_path, "r").read())
        self.abs_path = abs_path
        self.data = data

    def get_data(self):
        return self.data

    def update(self, data: dict, autoSave: bool = False):
        for key in data.keys():
            self.data[key] = data[key]
        if autoSave:
            self.save_changes()

    def save_changes(self):
        f = open(self.abs_path, "w")
        f.write(str(dict(self.data)).replace("'", "\""))
        f.close()


def get_path_to_collection(collectionKey):
    cpath = os.path.join(main.BASE_STORAGE_DIR, collectionKey)
    if os.path.exists(cpath):
        return cpath
    else:
        raise Exception('There is no collection key {}'.format(collectionKey))


def generate_collection_basis(collectionPath):
    d = json.loads((open(os.path.join(collectionPath, 'structure.json')).read()))
    fields = d['fields']
    basis = {}
    for field in fields:
        basis[field['name']] = field['type']
    return basis


def get_document(collectionKey, documentKey):
    cpath = get_path_to_collection(collectionKey)
    if os.path.exists(os.path.join(cpath, documentKey + ".json")):
        return Document(os.path.join(cpath, documentKey + ".json"))
    else:
        raise Exception('There is no document key {} in collection with key {}'.format(documentKey, collectionKey))


def validate_by_basis(collectionKey: str, dataset: dict):
    cpath = get_path_to_collection(collectionKey)
    basis = generate_collection_basis(cpath)
    for key in dataset:
        if key not in basis.keys():
            raise Exception('Field {} not in {}'.format(key, basis.keys()))
        if type(dataset[key]) is not locate(basis[key]):
            raise Exception('Field {} must be {} instead of {}'.format(key, basis[key], type(dataset[key])))
    return True


def get_all_documents(collectionKey):
    cpath = get_path_to_collection(collectionKey)
    keys = []
    if os.path.exists(cpath):
        for file in os.listdir(cpath):
            if 'structure' not in file:
                keys.append(file.split('.')[0])
        return keys
    else:
        return Exception('There is no collection key {}'.format(collectionKey))


# def get_data_by_query(collectionKey: str, query: dict):
#     cpath = get_path_to_collection(collectionKey)
#     if validate_by_basis(collectionKey, query):
#         for doc in os.listdir(cpath):
#             if '.' not in doc:
#                 print(doc)
#     else:
#         raise