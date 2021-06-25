#!/user/bin/python3
"""defines the class FileStorage

    TODO:
        obj.id is attribute or porperty??
"""

import json


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to
    instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if (obj is not None):
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionaries = {}

        for key, obj in self.all().items():
            dictionaries[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf8') as file:
            json.dump(dictionaries, file)

    def reload(self):
        """deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        """
        from models.base_model import BaseModel
        dictionaries = {}

        try:
            with open(FileStorage.__file_path, 'r') as file:
                dictionaries = json.load(file)
        except FileNotFoundError:
            return

        for key, each_dict in dictionaries.items():
            new_object = BaseModel(**each_dict)
            self.new(new_object)
