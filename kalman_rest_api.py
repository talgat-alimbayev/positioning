import json
from flask import Flask, request
from Tracker_KUIS import Tracker_KUIS

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
        trackers[name] = Tracker_KUIS(name, latitude, longitude)

    # changing latitude and longitude for filtered values
    data["latitude"] = trackers[name].getLat()
    data["longitude"] = trackers[name].getLong()

    return data
app.run(debug=True)