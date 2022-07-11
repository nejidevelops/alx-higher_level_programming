#!/usr/bin/python3
""" Module Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Object Builder """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def __str__(self):
        """ str repr """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, super().width))

    def update(self, *args, **kwargs):
        """ Assigns attr  """
        attr = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, attr[i], args[i])
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """ Instance to dictionary """
        obj_dict = {"id": self.id,
                    "size": self.size,
                    "x": self.x,
                    "y": self.y}
        return obj_dict
