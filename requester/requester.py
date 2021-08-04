import json

from .connection import Connection


class Requester:
    def __init__(self, connection: Connection):
        self.connection = connection

    def get(self, id: int) -> dict:
        return self.connection.select(id=id)

    def get_as_string(self, id: int) -> str:
        item = self.get(id=id)
        if item is not None:
            item = json.dumps(item)
        return item

    def get_all(self, id: int) -> list:
        raise NotImplementedError

    def create(self, data: dict) -> dict:
        try:
            self.connection.insert(data)
            return {"status": "OK"}
        except Exception:
            return {"status": "Error"}

    def update(self, id: int, data: dict):
        item = self.get(id=id)
        if not item:
            return {"status": "not_found"}

        item = {**item, **data, "id": id}

        try:
            self.connection.update(item)
            return {"status": "OK"}
        except Exception:
            return {"status": "Error"}

    def delete(self, id: int):
        raise NotImplementedError
