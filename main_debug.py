# This is a sample Python script.
import os
import json
import matplotlib.pyplot as plt

import numpy as np
from Beacon_navigen import Beacon_navigen
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

    xPos = np.array([])
    yPos = np.array([])

    # beaconList:{
    #              "ab8190d5d11e4941acc4ac233f5b8a0427114cb9", URL:4, (0,4190032925603682, 0,4496753246753247)
    #              "ab8190d5d11e4941acc4ac233f5b8a1327114cb9", URL:3, (0,5999896213914773, 0,5930343746672849)
    #              "ab8190d5d11e4941acc4ac233f5b88bd27114cb9", URL:3, (0,41919329135400984, 0,580019545143734)
    #              "fda50693a4e24fb1afcfac233f5b8a1227114cb9", URL:4, (0,6084157398821785, 0,5941558441558441)
    #              "fda50693a4e24fb1afcfac233f5b898f27114cb9", URL:3, (0,6018766125648648, 0,4728509241132918)
    #              "fda50693a4e24fb1afcfac233f5b8a0d27114cb9", URL:4, (0,3856973899775685, 0,5746541109949017)
    #              "fda50693a4e24fb1afcfac233f5b898b27114cb9", URL:4, (0,6329895756015409, 0,4515276185258065)
    # }
    beacons= {
            "ab8190d5d11e4941acc4ac233f5b8a0427114cb9": -40,
            "ab8190d5d11e4941acc4ac233f5b8a1327114cb9": -46,
            "ab8190d5d11e4941acc4ac233f5b88bd27114cb9": -43,
            "fda50693a4e24fb1afcfac233f5b8a1227114cb9": -55,
            "fda50693a4e24fb1afcfac233f5b898f27114cb9": -70,
            "fda50693a4e24fb1afcfac233f5b8a0d27114cb9": -78,
            "fda50693a4e24fb1afcfac233f5b898b27114cb9": -67
    }

    beacon1 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b8a1327114cb9', 0.5999896213914773, 0.5930343746672849, -48, 3.5)
    beacon2 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b88bd27114cb9', 0.41919329135400984, 0.580019545143734, -51, 3.5)
    beacon3 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b898f27114cb9', 0.6018766125648648, 0.4728509241132918, -50, 3.5)
    # beacon4 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b8a0427114cb9', 5.9, 5.2, -60, 4)
    # beacon5 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b88bd27114cb9', 5.9, 3.2, -60, 4)
    # beacon6 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b8a0927114cb9', 5.9, 1, -60, 4)
    # beacon7 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b898f27114cb9', 3, 0, -60, 4)
    # beacon8 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b8a0d27114cb9', 1.6, 0, -60, 4)


    # for i in range(N):
        # os.path.join(dir, list[i])
        # f = open(os.path.join(dir, list[i]), "r")
        # d = f.read()
        # data = json.loads(d)

    normCoef = 0

    for beacon in Beacon_navigen:
        beacon.setRssi(beacons[beacon.getID()])
        beacon.calculateDistance()
        normCoef += 1/np.abs(beacon.getDistance())

    Beacon_navigen.setNormCoef(normCoef)

    xPosIntermediate = 0
    yPosIntermediate = 0

    for beacon in Beacon_navigen:
        beacon.setWeight(1 / np.abs(beacon.getDistance() * Beacon_navigen.getNormCoef()))
        xPosIntermediate += beacon.getWeight() * beacon.getX()
        yPosIntermediate += beacon.getWeight() * beacon.getY()

    xPos = np.append(xPos, xPosIntermediate)
    yPos = np.append(yPos, yPosIntermediate)

    print(xPos, yPos)
    # plt.plot(xPos, yPos)
    # plt.plot(beacon1.getX(), beacon1.getY(), marker='o', ms=20)
    # plt.plot(beacon2.getX(), beacon2.getY(), marker='o', ms=20)
    # plt.plot(beacon3.getX(), beacon3.getY(), marker='o', ms=20)


    # plt.plot(beacon4.getX(), beacon4.getY(), marker='o', ms=20)
    # plt.plot(beacon5.getX(), beacon5.getY(), marker='o', ms=20)
    # plt.plot(beacon6.getX(), beacon6.getY(), marker='o', ms=20)
    # plt.plot(beacon7.getX(), beacon7.getY(), marker='o', ms=20)
    # plt.plot(beacon8.getX(), beacon8.getY(), marker='o', ms=20)
    # plt.legend(['tracker','window', 'in cupboard', 'on cabinet', 'locker', 'locker', 'locker', 'window', 'window'])
    #
    # plt.show()










