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

    beacon1 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b8a1227114cb9', 0, 0, -60, 4)
    beacon2 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b898b27114cb9', -0.7, 3.4, -60, 4)
    beacon3 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b8a1327114cb9', 0, 4.8, -60, 4)
    beacon4 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b8a0427114cb9', 5.9, 5.2, -60, 4)
    beacon5 = Beacon_navigen('ab8190d5d11e4941acc4ac233f5b88bd27114cb9', 5.9, 3.2, -60, 4)
    beacon6 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b8a0927114cb9', 5.9, 1, -60, 4)
    beacon7 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b898f27114cb9', 3, 0, -60, 4)
    beacon8 = Beacon_navigen('fda50693a4e24fb1afcfac233f5b8a0d27114cb9', 1.6, 0, -60, 4)

    # list_of_beacons = [beacon1, beacon2, beacon3, beacon4, beacon5, beacon6, beacon7, beacon8]


    # list_of_beacons = ['fda50693a4e24fb1afcfac233f5b8a1227114cb9',
    #                    'fda50693a4e24fb1afcfac233f5b898b27114cb9',
    #                    'ab8190d5d11e4941acc4ac233f5b8a1327114cb9',
    #                    'ab8190d5d11e4941acc4ac233f5b8a0427114cb9',
    #                    'ab8190d5d11e4941acc4ac233f5b88bd27114cb9',
    #                    'fda50693a4e24fb1afcfac233f5b8a0927114cb9',
    #                    'fda50693a4e24fb1afcfac233f5b898f27114cb9',
    #                    'fda50693a4e24fb1afcfac233f5b8a0d27114cb9']

    for i in range(N):
        os.path.join(dir, list[i])
        f = open(os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)

        beacon1.setRssi(data['beacons'][beacon1.getID()])
        beacon2.setRssi(data['beacons'][beacon2.getID()])
        beacon3.setRssi(data['beacons'][beacon3.getID()])
        beacon4.setRssi(data['beacons'][beacon4.getID()])
        beacon5.setRssi(data['beacons'][beacon5.getID()])
        beacon6.setRssi(data['beacons'][beacon6.getID()])
        beacon7.setRssi(data['beacons'][beacon7.getID()])
        beacon8.setRssi(data['beacons'][beacon8.getID()])

        beacon1.calculateDistance()
        beacon2.calculateDistance()
        beacon3.calculateDistance()
        beacon4.calculateDistance()
        beacon5.calculateDistance()
        beacon6.calculateDistance()
        beacon7.calculateDistance()
        beacon8.calculateDistance()

        normCoef = 1/np.abs(beacon1.getDistance()) + 1/np.abs(beacon2.getDistance()) + 1/np.abs(beacon3.getDistance()) + 1 / np.abs(beacon4.getDistance()) + 1/np.abs(beacon5.getDistance()) + 1/np.abs(beacon6.getDistance()) + 1 / np.abs(beacon7.getDistance()) + 1/np.abs(beacon8.getDistance())
        Beacon_navigen.setNormCoef(normCoef)

        beacon1.setWeight(1 / np.abs(beacon1.getDistance() * Beacon_navigen.getNormCoef()))
        beacon2.setWeight(1 / np.abs(beacon2.getDistance() * Beacon_navigen.getNormCoef()))
        beacon3.setWeight(1 / np.abs(beacon3.getDistance() * Beacon_navigen.getNormCoef()))
        beacon4.setWeight(1 / np.abs(beacon4.getDistance() * Beacon_navigen.getNormCoef()))
        beacon5.setWeight(1 / np.abs(beacon5.getDistance() * Beacon_navigen.getNormCoef()))
        beacon6.setWeight(1 / np.abs(beacon6.getDistance() * Beacon_navigen.getNormCoef()))
        beacon7.setWeight(1 / np.abs(beacon7.getDistance() * Beacon_navigen.getNormCoef()))
        beacon8.setWeight(1 / np.abs(beacon8.getDistance() * Beacon_navigen.getNormCoef()))

        xPos = np.append(xPos, beacon1.getWeight() * beacon1.getX() + beacon2.getWeight() * beacon2.getX() + beacon3.getWeight() * beacon3.getX() + beacon4.getWeight() * beacon4.getX() + beacon5.getWeight() * beacon5.getX() + beacon6.getWeight() * beacon6.getX() + beacon7.getWeight() * beacon7.getX() + beacon8.getWeight() * beacon8.getX())

        yPos = np.append(yPos, beacon1.getWeight() * beacon1.getY() + beacon2.getWeight() * beacon2.getY() + beacon3.getWeight() * beacon3.getY() + beacon4.getWeight() * beacon4.getY() + beacon5.getWeight() * beacon5.getY() + beacon6.getWeight() * beacon6.getY() + beacon7.getWeight() * beacon7.getY() + beacon8.getWeight() * beacon8.getY())

    plt.plot(xPos, yPos)
    plt.plot(beacon1.getX(), beacon1.getY(), marker='o', ms=20)
    plt.plot(beacon2.getX(), beacon2.getY(), marker='o', ms=20)
    plt.plot(beacon3.getX(), beacon3.getY(), marker='o', ms=20)
    plt.plot(beacon4.getX(), beacon4.getY(), marker='o', ms=20)
    plt.plot(beacon5.getX(), beacon5.getY(), marker='o', ms=20)
    plt.plot(beacon6.getX(), beacon6.getY(), marker='o', ms=20)
    plt.plot(beacon7.getX(), beacon7.getY(), marker='o', ms=20)
    plt.plot(beacon8.getX(), beacon8.getY(), marker='o', ms=20)
    plt.legend(['tracker','window', 'in cupboard', 'on cabinet', 'locker', 'locker', 'locker', 'window', 'window'])

    plt.show()










