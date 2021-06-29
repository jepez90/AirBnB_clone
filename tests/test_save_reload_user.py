#!/usr/bin/python3
"""basic tests for User class"""

import sys
import os
sys.path.append(os.path.abspath('..'))
from models import storage  # nopep8
from models.base_model import BaseModel  # nopep8
from models.user import User  # nopep8

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@holbertonshool.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
