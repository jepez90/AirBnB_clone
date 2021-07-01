#!/usr/bin/python3
"""Module for test the FileStorage class """

import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
    """

    def setUp(self):
        """function to config each test"""
        self.file_path = getattr(FileStorage, "_FileStorage__file_path")

    def tearDown(self):
        """function to end each test"""
        setattr(FileStorage, "_FileStorage__objects", {})

    def test_function_all(self):
        """ this function should return the dictionary __objects
        """
        setattr(FileStorage, "_FileStorage__objects", {})

        instance = FileStorage()
        self.assertEqual(instance.all(), {})

        setattr(FileStorage, "_FileStorage__objects", {"Hola", "Mundo"})
        self.assertEqual(instance.all(), {"Hola", "Mundo"})
        setattr(FileStorage, "_FileStorage__objects", {})

        base_model_instance1 = BaseModel()
        base_model_instance2 = BaseModel()
        base_model_instance3 = BaseModel()
        self.assertEqual(len(instance.all()), 3)

    def test_function_new(self):
        """ sets in __objects the obj with key <obj class name>.id
        """

        setattr(FileStorage, "_FileStorage__objects", {})

        """ the dict __object is void """
        instance = FileStorage()
        self.assertEqual(instance.all(), {})

        """ the dict __object has an BaseModel element """
        base_model_instance = BaseModel()
        self.assertEqual(len(instance.all()), 1)

        """ the key of the BaseModel element is correct """
        list_objects = instance.all()
        key = "BaseModel." + str(base_model_instance.id)
        self.assertEqual(base_model_instance, list_objects[key])

    def test_function_save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """

        """ the dict __object is void and file doesn't exist"""
        instance = FileStorage()
        instance.save()

        """create the file if it doesn't exist"""
        self.assertTrue(os.path.exists(self.file_path))

        """ write the correct output """
        with open(self.file_path, 'r') as file:
            json_string = json.load(file)
        self.assertEqual(json_string, {})

        base_model_instance1 = BaseModel()
        base_model_instance2 = BaseModel()
        instance.save()
        base_model_instance3 = BaseModel()
        instance.save()

        key = "BaseModel." + str(base_model_instance2.id)
        with open(self.file_path, 'r') as file:
            json_string = json.load(file)

        self.assertEqual(json_string[key], base_model_instance2.to_dict())

    def test_function_reload(self):
        """ deserializes the JSON file to __objects
        """

        instance = FileStorage()

        """ the file don't contains serialized objets """
        with open(self.file_path, 'w', encoding='utf8') as file:
            json.dump("{}", file)

        instance.reload()

        self.assertEqual(len(instance.all()), 0)

        """ the file contains two serialized objets """

        string = '{"BaseModel.055de01b": {"id": "055de01b", "created_at":'\
            + '"2021-06-26T21:43:11.896838", "updated_at":'\
            + '"2021-06-26T21:43:11.896885", "name": "Holberton",'\
            + '"my_number": 89, "__class__": "BaseModel"},'\
            + '"BaseModel.4749f227": {"id": "4749f227", "created_at":'\
            + '"2021-06-26T21:43:29.787034", "updated_at":'\
            + '"2021-06-26T21:43:29.787079", "name": "Holberton",'\
            + '"my_number": 89, "__class__": "BaseModel"}}'
        key = 'BaseModel.055de01b'

        with open(self.file_path, 'w', encoding='utf8') as file:
            file.write(string)

        instance.reload()
        self.assertEqual(len(instance.all()), 2)
        obj = instance.all()[key]
        self.assertEqual(obj.id, "055de01b")

        """ if the file doesn't exist """
        if (os.path.exists(self.file_path)):
            os.remove(self.file_path)
        setattr(FileStorage, "_FileStorage__objects", {})

        instance.reload()
        self.assertEqual(instance.all(), {})
