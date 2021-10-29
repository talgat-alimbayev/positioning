import json
from flask import Flask, request, jsonify
from Tracker_KUIS import Tracker_KUIS

app = Flask(__name__)
trackers = {}

@app.route('/', methods=['POST'])
def process_coordinates():
    print("Hello world!")
    # data = request.get_json()
    print(request.json.get("protocol_version"))
    return 1

    # data = json.loads(request.get_json())
    #
    # name = data["device_imei"]
    # latitude = data["msg"]["sub_packet_1_data"]["values"]["latitude"]
    # longitude = data["msg"]["sub_packet_1_data"]["values"]["longitude"]
    # if name in trackers:
    #     trackers[name].setMeas(latitude, longitude)
    #     trackers[name].kalmanFilter()
    # else:
    #     trackers[name] = Tracker_KUIS(name, latitude, longitude)
    #
    # # changing latitude and longitude for filtered values
    # data["msg"]["sub_packet_1_data"]["values"]["latitude"] = trackers[name].getLat()
    # data["msg"]["sub_packet_1_data"]["values"]["longitude"] = trackers[name].getLong()
    #
    #
    # return jsonify(data)
try:
    app.run(debug=True)
except Exception as e:
    print("An exception occurred: %s", e)
