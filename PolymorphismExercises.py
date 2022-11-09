#Challange 1

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name
        self.sname = super().getName()

    def getName(self):  # overriden method
        return (self.sname + ", " + self.xsname)



#Challange 2
class Animal:
    pass
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details(test):
        print("Name: ", self.name)
        print("Sound: ", self.sound)


class Dog(Animal):
    pass
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details(test):
        super().Animal_details()
        print("Family: ", self.family)

class Sheep(Animal):
    pass
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(test):
        super().Animal_details()
        print("Color: ", self.color)
