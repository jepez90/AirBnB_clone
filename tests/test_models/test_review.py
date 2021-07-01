#!/usr/bin/python3
"""Module for test the Review class """

import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
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

    def test_attributes(self):
        """ this function should return the dictionary __objects
        """
        pass
