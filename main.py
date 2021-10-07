# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from Beacon import Beacon


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    beacon1 = Beacon("beacon1", -89, 2, 5, -50, 4)
    print(beacon1.getDistance())
    print(beacon1.getX())
    print(beacon1.getY())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
