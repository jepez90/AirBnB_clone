#!/usr/bin/python3
""" test_base_model.py """
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel Class """

    @classmethod
    def setUpClass(cls):
        """ Instance the class and assigns value to attributes """
        cls.base_model = BaseModel()
        cls.base_model.name = "Holberton"
        cls.base_model.my_number = 89

    @classmethod
    def teardown(cls):
        """ Delete Base Model Class """
        del cls.base_model
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_methods(self):
        """ Validates class methods """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """ validates if the object is an instance of the class BaseModel """
        self.assertTrue(isinstance(self.base_model, BaseModel))

    def test_str(self):
        """ verifies that the string contains the attributes of class """
        base_str = str(self.base_model)
        self.assertEqual(True, "[BaseModel] ({})".format(
            self.base_model.id) in base_str)
        self.assertEqual(True, "created_at" in base_str)
        self.assertEqual(True, "updated_at" in base_str)
        self.assertEqual(True, "datetime.datetime" in base_str)

    def test_save(self):
        """ Check save method """
        update = self.base_model.updated_at
        time_updated = os.path.getmtime('file.json')
        self.base_model.save()
        self.assertNotEqual(update, self.base_model.updated_at)
        self.assertTrue(os.path.exists('file.json'))
        # print("last modified: %s" % time.ctime(os.path.getmtime(file)))
        self.assertNotEqual(os.path.getmtime('file.json'), time_updated)

    def test_to_dict(self):
        """ Check dictionary method """
        bm_dict = self.base_model.to_dict()
        self.assertEqual(self.base_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
        self.assertEqual(type(bm_dict), dict)


if __name__ == "__main__":
    unittest.main()
