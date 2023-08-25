#!/usr/bin/python3
"""
Class Square
"""


from inspectimport classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that defines square properties
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        instances of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        print square representation
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x,
                       self.y, self.size))

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        arguments of each attribute
        """
        if args is not None and len(args) is not 0:
            attr_list = ["id", "size", "x", "y"]
            for x in range(len(args)):
                if attr_list[x] = "size":
                    setattr(self, "width", args[x])
                    setattr(self, "height", args[x])
                else:
                    setattr(self, attr_list[x], args[x])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        A dictionary representation of a square
        """
        dictS = self.__dict__
        dictSq = {}
        dictSq["id"] = dictS["id"]
        dictSq["size"] = dictS["_Rectangle__width"]
        dictSq["x"] = dictS["_Rectangle__x"]
        dictSq["y"] = dictS["_Rectangle__y"]

        return dictSq
