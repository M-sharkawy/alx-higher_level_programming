#!/usr/bin/python3

"""Model for class rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle subclass inherits attributes from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiation method

            args:
                width (int) = rectangle width
                height (int) = rectangle height
                x (int) = x value
                y (int) = y value
                id (int) = id number
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width asign method"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter value"""
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(width) != int:
            raise TypeError("width must be an integer")
        
        self.__width = width

    @property
    def height(self):
        """height asign method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter value"""
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """x asign method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter value"""
        if value < 0:
            raise ValueError("x must be >= 0")
        if type(value) != int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """x asign method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter value"""
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) != int:
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        area = self.width * self.height
        return area

    def display(self):
        """print the rectangle using # """
        print("\n" * self.y, end="")
        for index in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
            if args:
                for index, arg in enumerate(args):
                    if index == 0:
                        self.id = arg
                    if index == 1:
                        self.__width = arg
                    if index == 2:
                        self.__height = arg
                    if index == 3:
                        self.__x = arg
                    if index == 4:
                        self.__y = arg
            else:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "width":
                        self.__width = value
                    if key == "height":
                        self.__height = value
                    if key == "x":
                        self.__x = value
                    if key == "y":
                        self.__y = value

    def to_dictionary(self):
        """return dict representation of Rectangle"""
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
