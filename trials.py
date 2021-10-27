import numpy as np
class IterableCar(type):
    def __iter__(cls):
        return iter(cls.__name__)

class Car(metaclass=IterableCar):
    __metaclass__ = IterableCar

    def __init__(self, name):
        self.name = name


if __name__=='__main__':

    car1 = Car('Mercedes')
    car2 = Car('Toyota')
    for cars in Car:
        print (cars)

    print(np.version.version)