#!/user/bin/python3
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
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """ Update the update_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary """
        my_dict = self.__dict__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
