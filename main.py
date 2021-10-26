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

    rssi_1m = -60
    N_env = 4

    beacon_on_cabinet25 = Beacon_kalman('ab8190d5d11e4941acc4ac233f5b8a0427114cb9', 0, 0, rssi_1m, N_env)
    rssi_before_KF = np.array([])
    rssi_after_KF = np.array([])

    x_axis = np.array([])

    for i in range(N):
        os.path.join(dir, list[i])
        f = open(os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)
        x = data['beacons']['ab8190d5d11e4941acc4ac233f5b8a0427114cb9']

        beacon_on_cabinet25.setRssi(x)
        beacon_on_cabinet25.KalmanFilter()
        beacon_on_cabinet25.calculateDistance()

        rssi_before_KF = np.append(rssi_before_KF, x)
        rssi_after_KF = np.append(rssi_after_KF, beacon_on_cabinet25.getRssiEst())

        x_axis = np.append(x_axis, i)

    plt.plot(x_axis, rssi_before_KF)
    plt.plot(x_axis, rssi_after_KF)
    plt.legend(["RSSI before KF", "RSSI after KF"])
    plt.title('RSSI readings from stationary beacon')
    plt.show()




    sum = 0.0
    for i in range(rssi_after_KF.shape[0]):
        x = rssi_after_KF[i]
        sum = sum + x

    mean = sum/N
    variance = 0

    for i in range(rssi_after_KF.shape[0]):
        variance = variance + (rssi_after_KF[i] - mean) ** 2

    variance = variance / (N - 1)
    print("mean: ", mean)
    print("variance: ", variance)




