#!/usr/bin/python3
"""
defines a class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    Attr:
    __file_path - string - path to the JSON file
    __objects - dictionary - empty but will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
7
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        our_dict = {}
        for key, value in self.__objects.items():
            our_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            my_file.write(json.dumps(our_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as my_file:
                our_dict = json.load(my_file)
                for obj in our_dict.items():
                    cls_name = obj["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
