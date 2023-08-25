#!/usr/bin/python3
"""
Class rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    defines properties of rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instances of rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """
        print rectangle
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x,
                       self.__y, self.__width, self.__height))

    @property
    def width(self):
        """
        get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        get x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        get y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints rectangle in stdout with the character #
        """
        if self.__y > 0:
            for k in range(self.__y):
                print()
            self.__y = 0
        for row in range(self.__height):
            for col in range(self.__width):
                if self.__y == col:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        args and kwargs
        """
        if args in not None and len(args) is not 0:
            attr_list = ["id", "width", "height", "x", "y"]
            for x in range(len(args)):
                setattr(self, attr_list[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        A dictionary representation of a rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
