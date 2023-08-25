#!/usr/bin/python3
"""
Define a base class
"""
import json
import os.path


class Base:
    """
    Class of base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Create an instance of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Json string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictinaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes Json string representation of list objects to file
        """
        filename = "{}.json".format(cls.__name__)
        dict_list = []

        if not list_objs:
            pass
        else:
            for x in range(len(list_objs)):
                dict_list.append(list_objs[x].to_dictionary())

        lis_dict = cls.to_json_string(dict_list)

        with open(filename, "w") as file_name:
            file_name(lis_dict)

    @staticmethod
    def from_json_string(json_string):
        """
        list of json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as file_name:
            str_list = file_name.read()

        cls_list = cls.from_json_string(str_list)
        ins_list = []

        for i in range(len(cls_list)):
            ins_list.append(cls.create(**cls_list[i]))

        return (ins_list)
