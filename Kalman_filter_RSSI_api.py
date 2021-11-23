app = Flask(__name__)
trackers = {}

@app.route('/filterCoordinates', methods=['POST'])
def process_coordinates():
    data = request.get_json(force=True)

    deviceName = data["deviceName"]
    beacons = data["beaconList"]

    if deviceName not in trackers:
        trackers[deviceName] = {}

    for beacon in beacons:
        if 

    if deviceName in trackers:
        trackers[name].setMeas(latitude, longitude)
        trackers[name].kalmanFilter()
    else:
        trackers[name] = Kalman_filter(name, latitude, longitude)

    # changing latitude and longitude for filtered values
    data["latitude"] = trackers[name].getLat()
    data["longitude"] = trackers[name].getLong()

    return data

@app.route('/getDebugData', methods=['POST'])
def getDebugData():
    data = request.get_json(force=True)
    name = data["id"]
    # return trackers[name].getDebug()

    print(trackers[name].getDebug())

    return data

app.run(host='0.0.0.0', port=3022)