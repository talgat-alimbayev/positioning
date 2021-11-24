import os
import json

from Kalman_filter_RSSI import Kalman_filter_RSSI

if __name__ == '__main__':

    dir = r"C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\kalman_filter_RSSI"
    list = os.listdir(dir)
    N = len(list)  # number of json files
    trackers = {}

    for i in range(N):
        # this code is only to read files which we won't need on the server
        f = open(os.path.join(dir, list[i]), "r")
        data = json.loads(f.read())


        deviceName = data["deviceName"]
        beacons = data["beaconList"] # list of beacons in the current message

        # first check if tracker exists in the dictionary with trackers and create it if it doesn't
        if deviceName not in trackers:
            trackers[deviceName] = {}
        else:
            beacons_in_memory = set(trackers[deviceName].keys()) # beacons in the memory from the previous
                                                                 # message converted to a set
            beacons_to_remove = beacons_in_memory.difference(beacons) # find beacons only present in the memory
                                                                      # and not in the current message, i.e. effectively
                                                                      # find beacons no longer in the range
            for key_to_remove in beacons_to_remove:
                del trackers[deviceName][key_to_remove]

        # create beacons if they don't exist and perform kalman filtering
        for beacon in beacons:
            rssi_meas = data["beacons"][beacon]
            if beacon in trackers[deviceName]:
                trackers[deviceName][beacon].setRssi(rssi_meas)
                trackers[deviceName][beacon].kalmanFilter()
            else:
                trackers[deviceName][beacon] = Kalman_filter_RSSI(rssi_meas, deviceName, beacon)

        print(trackers[deviceName].keys())