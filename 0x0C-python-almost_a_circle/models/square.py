#!usr/bin/python3

"""module of Squar Class inherits from the Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Squar Class inherits from the Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size ,size, x, y, id)
    
    def __str__(self):
        """string representation of the instances"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size asign method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter value"""
        if int(value) <= 0:
            raise ValueError("width must be > 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributs according to the input"""
        if args:
            for i,arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dict representation of the square instance"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
                        