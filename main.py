from fastapi import FastAPI

import utils
from logs.logger import Logger
import storage
import os
from APIBody import *

app = FastAPI()

# BASES
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_LOG_DIR = os.path.join(BASE_DIR, 'logs')
BASE_STORAGE_DIR = os.path.join(BASE_DIR, 'storage')

# LOGGING
LOGGER = Logger(baseDir=BASE_LOG_DIR)


@app.post("/test")
def test_endpoint(body: TestBody):
    LOGGER.debug('test_endpoint')
    return body.dict()


@app.post("/storage/collection")
def collection_endpoint(collectionData: CollectionCreateData):
    LOGGER.debug('collection_endpoint')
    r = storage.new_collection(collectionData)
    return {"ok": r}


@app.post('/storage/{collectionKey}/data')
def put_data_endpoint(collectionKey: str, body: BaseBody):
    try:
        r, key = storage.put_data(collectionKey, body.payload)
        return {"ok": r, "documentKey": key}
    except Exception as err:
        return {"error": err.__str__()}


@app.patch('/storage/{collectionKey}/{documentKey}')
def edit_data_endpoint(collectionKey: str, documentKey: str, body: BaseBody):
    try:
        r = storage.update_data(collectionKey, documentKey, body.payload)
        return {'ok': r}
    except Exception as err:
        return {"error": err.__str__()}


@app.get('/storage/{collectionKey}/{documentKey}')
def get_data_by_key(collectionKey: str, documentKey: str):
    try:
        return storage.get_data(collectionKey, documentKey)
    except Exception as err:
        return {"error": err.__str__()}


@app.get('/storage/{collectionKey}/query/make')
def get_data_by_query(collectionKey: str, body: BaseBody):
    data = body.payload
    docs = storage.get_documents_list_by_query(collectionKey, data['query'])
    res = []
    for doc in docs:
        res.append(doc.get_data())
    return res
