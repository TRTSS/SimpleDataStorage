import json
import os
import random
import string

import main
import utils


def new_collection(collectionStructure):
    data = collectionStructure.dict()
    collectionPath = os.path.join(main.BASE_STORAGE_DIR, data['key'])
    print(str(collectionStructure))
    if not os.path.exists(collectionPath):
        os.makedirs(collectionPath, exist_ok=True)
        structFile = open(os.path.join(str(collectionPath), 'structure.json'), 'w')
        structFile.write(str(collectionStructure.dict()).replace("'", "\""))
        structFile.close()
        return True
    return False


def put_data(collectionKey, data):
    collectionPath = utils.get_path_to_collection(collectionKey)
    if os.path.exists(collectionPath):
        key = random.choices(string.ascii_letters + string.digits, k=10)
        key = "".join(key)
        if utils.validate_by_basis(collectionKey, data):
            dataFile = open(os.path.join(str(collectionPath), key + ".json"), 'w')
            dataFile.write(json.dumps(data))
            dataFile.close()
            return True, key
    raise Exception('Collection does not exist')


def update_data(collectionKey, documentKey, data):
    if utils.validate_by_basis(collectionKey, data):
        doc = utils.get_document(collectionKey, documentKey)
        doc.update(data, autoSave=True)
        return True
    else:
        raise Exception('Update data is not valid')


def get_data(collectionKey, documentKey):
    doc = utils.get_document(collectionKey, documentKey)
    return doc.get_data()


def get_documents_list_by_query(collectionKey, query):
    keys = utils.get_all_documents(collectionKey)
    docs = [utils.get_document(collectionKey, x) for x in keys]
    queriedDocs = []
    for doc in docs:
        d = dict(doc.get_data())
        f = True
        for orQ in query:
            flag = True
            for andQ in orQ:
                if andQ in d.keys():
                    if orQ[andQ] != d[andQ]:
                        flag = False
                        break
            f = flag
        if f:
            queriedDocs.append(doc)

    return queriedDocs

