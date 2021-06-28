#!/usr/bin/python3
""" class user """
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel

    Args:
        BaseModel (Class): class basemodel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initialize inherited attributes """
        super().__init__(*args, **kwargs)
