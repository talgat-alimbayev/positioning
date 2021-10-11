# This is a sample Python script.
import os
import json
import matplotlib.pyplot as plt

import numpy as np
from Beacon_kalman import Beacon_kalman
from Variance import variance

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Just put r before your normal string it converts normal string to raw string:
    # variance(r'C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\Positioning\PositionLogs\1_centerOfTheRoom')
    dir = r'C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\Positioning\PositionLogs\1_centerOfTheRoom'
    list = os.listdir(dir)
    N = len(list)  # number of samples to calculate variance


    for i in range(N):
        os.path.join(dir, list[i])
        f = open(os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)







