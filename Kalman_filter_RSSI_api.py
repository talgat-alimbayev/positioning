from flask import Flask, request
from Kalman_filter_RSSI import Kalman_filter_RSSI

app = Flask(__name__)
trackers_ble = {}

@app.route('/filterRssi', methods=['POST'])
def process_rssi():
    data = request.get_json(force=True)

    deviceName = data["deviceName"]
    beacons = data["beaconList"]

    # first check if tracker exists in the dictionary with trackers and create it if it doesn't
    if deviceName not in trackers_ble:
        trackers_ble[deviceName] = {}
    else:
        beacons_in_memory = set(trackers_ble[deviceName].keys())  # beacons in the memory from the previous
                                                              # message converted to a set
        beacons_to_remove = beacons_in_memory.difference(beacons)  # find beacons only present in the memory
                                                                   # and not in the current message, i.e. effectively
                                                                   # find beacons no longer in the range
    for beacon_to_remove in beacons_to_remove:
        del trackers_ble[deviceName][beacon_to_remove]

    # create beacons if they don't exist and perform kalman filtering
    for beacon in beacons:
        rssi_meas = data["beacons"][beacon]
        if beacon in trackers_ble[deviceName]:
            trackers_ble[deviceName][beacon].setRssi(rssi_meas)
            trackers_ble[deviceName][beacon].kalmanFilter()
            data["beacons"][beacon] = trackers_ble[deviceName][beacon].getRssiEst()
        else:
            trackers_ble[deviceName][beacon] = Kalman_filter_RSSI(rssi_meas, deviceName, beacon)

    return data

@app.route('/getDebugData', methods=['POST'])
def getDebugData():
    data = request.get_json(force=True)
    name = data["id"]
    # return trackers[name].getDebug()

    print(trackers[name].getDebug())

    return data

app.run(host='0.0.0.0', port=3022)