import os
import json
import matplotlib.pyplot as plt

import numpy as np
from Kalman_filter_RSSI import Kalman_filter_RSSI

if __name__ == '__main__':

    dir = r"C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\kalman_filter_RSSI"
    list = os.listdir(dir)
    # print(list)
    N = len(list)  # number of json files
    trackers = {}

    for i in range(N):
        # this code is only to read files which we won't need on the server
        f = open(os.path.join(dir, list[i]), "r")
        data = json.loads(f.read())


        deviceName = data["deviceName"]
        beacons = data["beaconList"]

        # first check if tracker exists in the dictionary with trackers
        if deviceName not in trackers:
            trackers[deviceName] = {}






        # check for beacons that are not visible
        beacons_to_remove=[]
        for beacon_remove in trackers[deviceName]:
            if beacon_remove not in beacons:
                beacons_to_remove.append(beacon_remove)

        # remove the beacons that are not visible
        for key_to_remove in beacons_to_remove:
            del trackers[deviceName][key_to_remove]

        # create beacons if they don't exist and perform kalman filtering
        for beacon in beacons:
            rssi_meas = data["beacons"][beacon]
            if beacon in trackers[deviceName]:
                trackers[deviceName][beacon].setRssi(rssi_meas)
                trackers[deviceName][beacon].KalmanFilter()
            else:
                trackers[deviceName][beacon] = Kalman_filter_RSSI(rssi_meas, deviceName, beacon)


            # print(beacon, trackers[deviceName][beacon].getRssiEst())
        # print(trackers)


    # if deviceName in trackers:
    #     trackers[name].setMeas(latitude, longitude)
    #     trackers[name].kalmanFilter()
    # else:
    #     trackers[name] = Kalman_filter(name, latitude, longitude)
    #
    # # changing latitude and longitude for filtered values
    # data["latitude"] = trackers[name].getLat()
    # data["longitude"] = trackers[name].getLong()
    #
    # return data