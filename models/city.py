#!/usr/bin/python3
"""Module class city.py"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City that inherits from BaseModel

    Args:
        BaseModel (class): SuperClass
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization point inherit super class"""
        super().__init__(*args, **kwargs)
