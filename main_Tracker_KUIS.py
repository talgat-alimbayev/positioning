import json
import os

import matplotlib.pyplot as plt
import numpy as np
from Tracker_KUIS import Tracker_KUIS
def jsonfy(s:str)->object:
    #This function normalizes the key of json without double quotes
    obj = eval(s, type('js', (dict,), dict(__getitem__=lambda s, n: n))())
    return obj

if __name__ == '__main__':
    # ####################################################################################
    # # Working filter code
    # dir = r"C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\КУИС\Logs_variance"
    # list = os.listdir(dir)
    # N = len(list)  # number of samples to calculate variance
    #
    # f = open(os.path.join(dir, list[0]), "r")
    # d = f.read()
    # data = json.loads(d)
    # name = data["device_imei"]
    # lat_init = data["msg"]["sub_packet_1_data"]["values"]["latitude"]
    # long_init = data["msg"]["sub_packet_1_data"]["values"]["longitude"]
    # tracker = Tracker_KUIS(name, lat_init, long_init)
    #
    # latitude_nofilter = np.array([])
    # latitude_filter = np.array([])
    #
    # longitude = np.array([])
    # for i in range(N):
    #     f = open( os.path.join(dir, list[i]), "r")
    #     d = f.read()
    #     data = json.loads(d)
    #     tracker.setMeas(data["msg"]["sub_packet_1_data"]["values"]["latitude"], data["msg"]["sub_packet_1_data"]["values"]["longitude"])
    #     tracker.kalmanFilter()
    #     print(data["msg"]["sub_packet_1_data"]["values"]["latitude"],tracker.getLat())
    #     latitude_nofilter = np.append(latitude_nofilter, data["msg"]["sub_packet_1_data"]["values"]["latitude"])
    #     latitude_filter = np.append(latitude_filter, tracker.getLat())
    #     longitude = np.append(longitude, tracker.getLong())
    #
    # plt.plot(latitude_filter)
    # plt.plot(latitude_nofilter)
    # plt.legend(["latitude filter", "latitude no filter"])
    # plt.title('latitude')
    # plt.show()
    # # Working filter code
    # ####################################################################################
    #
    dir = r"C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\КУИС\json_tests"
    list = os.listdir(dir)
    print(list)
    N = len(list)  # number of samples to calculate variance
    trackers = {}
    for i in range(N):
        # this code is only to read files which we won't need on the server
        f = open(os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)
        print("data before filterting", "device_imei: ", data["device_imei"],
              "ts: ", data["msg"]["sub_packet_1_data"]["ts"],
              "latitude: ", data["msg"]["sub_packet_1_data"]["values"]["latitude"],
              "longitude: ", data["msg"]["sub_packet_1_data"]["values"]["longitude"])
        # the above code is not needed on the server
        name = data["device_imei"]
        latitude = data["msg"]["sub_packet_1_data"]["values"]["latitude"]
        longitude = data["msg"]["sub_packet_1_data"]["values"]["longitude"]
        if name in trackers:
            trackers[name].setMeas(latitude, longitude)
            trackers[name].kalmanFilter()
        else:
            trackers[name] = Tracker_KUIS(name,latitude, longitude)

        # changing latitude and longitude for filtered values
        data["msg"]["sub_packet_1_data"]["values"]["latitude"] = trackers[name].getLat()
        data["msg"]["sub_packet_1_data"]["values"]["longitude"] = trackers[name].getLong()
        print("data after filterting", "device_imei: ", data["device_imei"],
              "ts: ", data["msg"]["sub_packet_1_data"]["ts"],
              "latitude: ", data["msg"]["sub_packet_1_data"]["values"]["latitude"],
              "longitude: ", data["msg"]["sub_packet_1_data"]["values"]["longitude"])
