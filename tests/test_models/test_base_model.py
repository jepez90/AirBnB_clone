#!/usr/bin/python3
""" test_base_model.py """
import os
import pep8
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

    def test_pep8_User(self):
        """ Check pep8 """
        psg = pep8.StyleGuide(quiet=True)
        model = "models/base_model.py"
        tests = "tests/test_models/test_base_model.py"
        results = psg.check_files([model, tests])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """ Check documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

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
        self.base_model.save()
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """ Check dictionary method """
        bm_dict = self.base_model.to_dict()
        self.assertEqual(self.base_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
        self.assertEqual(type(bm_dict), dict)


if __name__ == "__main__":
    unittest.main()
