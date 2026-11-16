#Realization
from abc import ABC, abstractmethod


class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Drawable):

    def draw(self):
        print("Drawing a circle.")


shape = Circle()
shape.draw()