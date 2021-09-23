from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = 'default.json'

    @abstractmethod
    def save(self):
        obj_in_dict_format = self._generate_dict()
        objs = self.get_file_data(self.file)
        objs.append(obj_in_dict_format)
        self.save_to_file(objs)

    @abstractmethod
    def _generate_dict(self):
        pass

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id:
                return el

        raise Exception("Not found")

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        with open("database/" + file_name, 'r') as file:
            data = json.loads(file.read())
            return data

    def save_to_file(self, data):
        data = json.dumps(data)
        with open('database/' + self.file, "w") as file:
            file.write(data)
