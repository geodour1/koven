from typing import Self


class User:
    id: str
    name: str

    def __init__(self, id: str = None, name: str = None) -> Self:
        self.id = id
        self.name = name

    @classmethod
    def from_doc(cls, doc: dict) -> Self:
        id = str(doc.get('_id', ""))
        name = doc.get('name', "")
        return User(id, name)

    def to_json(self, include_id=False) -> dict:
        data = {
            "name": self.name
        }

        if include_id:
            data["id"] = self.id

        return data
