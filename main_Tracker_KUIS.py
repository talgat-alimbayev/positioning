import json
from Tracker_KUIS import Tracker_KUIS
def jsonfy(s:str)->object:
    #This function normalizes the key of json without double quotes
    obj = eval(s, type('js', (dict,), dict(__getitem__=lambda s, n: n))())
    return obj

if __name__ == '__main__':
    # data = '{sub_packet_1_data: {ts: 1635318881000,values: {sub_packet_type: '01', device_name: '1234', gps_sign: '3D fixed', latitude: 43.229044, longitude: 76.931784, BuiltIn_Battery_Voltage: '4.153', Motion_Status: 'Stationary', GSM_Anti_Jamming: 'Normal', Domestic_roaming: 'No', International_Roaming: 'No', Geo_fence_Alarm: 'No', Rest_Status: 'Yes', Privat_Status: 'No', Fiber_Optical_Status: 'Connected', Battery_Low_Voltage_Status: 'No', Battery_Under_Voltage_Status: 'No', Body_Gesture: 'Lie down', Charge_Status: 'Not Charge', Lock_Status: 'Lock Status', Ibeacon_Status: 'Exit' }  }  }'
    # data = jsonfy(data)
    # s = '{symbol:"sh600069",code:"600069",name:"Silver Pigeon Investment",trade:"3.160",pricechange:"-0.030",changepercent:"-0.940",buy:"3.160", Sell:"3.170",settlement:"3.190",open:"3.190",high:"3.210",low:"3.140",volume:3905810,amount:12388386,ticktime:"15:00:00",per: 79, pb: 2.416, mktcap: 513131.494704, nmc: 513131.494704, turnoverratio: 0.24053}'
    # s = jsonfy(s)
    f = open("C:/Users/tyalimbayev/Desktop/Code/positioning/test_message_KUIS.json", "r")
    data = json.loads(f.read())
    trackers = {}
    trackers[(data["sub_packet_1_data"]["values"]["device_name"]) ] = Tracker_KUIS( (data["sub_packet_1_data"]["values"]["device_name"]), (data["sub_packet_1_data"]["values"]["latitude"]), (data["sub_packet_1_data"]["values"]["longitude"]))
    print(trackers["1234"].getMeas())
