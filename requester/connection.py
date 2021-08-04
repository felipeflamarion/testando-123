class Connection:
    def select(id: int) -> dict:
        raise NotImplementedError

    def select_all() -> list:
        raise NotImplementedError

    def insert(data: dict):
        raise NotImplementedError

    def update(data: dict):
        raise NotImplementedError

    def delete(id: int):
        raise NotImplementedError
