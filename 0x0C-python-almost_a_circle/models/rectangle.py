#!/usr/bin/python3
""" Module Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Object Builder """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ __width getter """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        """ __width setter """
        self.__width = width

    @property
    def height(self):
        """ __height getter  """
        return self.__height

    @height.setter
    def height(self, height):
        """ __height setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ __x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ __x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ __y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ __y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Returns the area """
        return self.__height * self.__width

    def display(self):
        """ Prints self  """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns str repr """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Assigns args to each attr """
        attr = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args:
            if len(args) <= 5:
                for i in range(len(args)):
                    setattr(self, attr[i], args[i])
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """ Instance to dictionary """
        obj_dict = {"id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y}
        return obj_dict
