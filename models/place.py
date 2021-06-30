#!/usr/bin/python3
"""Module class place.py"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place that inherits from BaseModel

    Args:
       BaseModel (class): SuperClass
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialization point inherit super class"""
        super().__init__(*args, **kwargs)
