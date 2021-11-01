import json
from flask import Flask, request
from Kalman_filter import Kalman_filter

app = Flask(__name__)
trackers = {}

@app.route('/', methods=['POST'])
def process_coordinates():
    data = request.get_json(force=True)

    name = data["id"]
    latitude = data["latitude"]
    longitude = data["longitude"]

    if name in trackers:
        trackers[name].setMeas(latitude, longitude)
        trackers[name].kalmanFilter()
    else:
        trackers[name] = Kalman_filter(name, latitude, longitude)

    # changing latitude and longitude for filtered values
    data["latitude"] = trackers[name].getLat()
    data["longitude"] = trackers[name].getLong()

    return data
app.run(debug=True)