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
    def width(self, value):
        """width setter value"""
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        
        self.__width = value

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
        """Display rectangle of '#' according to width and height""" 
        i = 0
        while (i < self.height):
            j = 0
            while (j < self.width):
                print("#", end="")
                j += 1
            print("")
            i += 1
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
