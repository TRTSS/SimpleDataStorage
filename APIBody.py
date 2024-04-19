from pydantic import BaseModel


class CollectionCreateData(BaseModel):
    name: str
    key: str
    fields: list


class BaseBody(BaseModel):
    payload: dict


class TestBody(BaseModel):
    text: str
    body: dict
