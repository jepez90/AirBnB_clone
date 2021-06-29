#!/user/bin/python3
"""This module defines the BaseModel class"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ Class BaseModel """

    def __init__(self, *args, **kwargs):
        """ Init method """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    time = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, time)
                else:
                    if (key != "__class__"):
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """__str__

        Returns:
            string: should print [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        self_id = self.id
        self_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self_id, self_dict)

    def save(self):
        """ Update the update_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
