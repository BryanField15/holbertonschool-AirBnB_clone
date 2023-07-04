#!/usr/bin/python3
"""Module with class Base"""

import json
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize class attibutes"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints formatted string"""
        return (f"[{type(self)}] ({self.id}) {self.to_dict()}")

    def save(self):
        """Updates public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of an instance """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        return new_dict
