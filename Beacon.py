import numpy as np

class Beacon:

    def __init__(self, id, rssi, x, y, rssi_1m, N):
        self.id = id
        self.rssi = rssi
        self.x = x
        self.y = y
        self.rssi_1m = rssi_1m #RSSI at one meter distance, needs to be calibrated for each beacon
        self.N = N #N is a path loss coefficient. The more obstacles there are, the larger it will be
        self.d = 10 ** ( (rssi_1m - rssi) / (10*N) )
        self.rssi_prev = 0

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getDistance(self):
        return self.d
    def getN(self):
        return self.N

    def setRssi(self, rssi):
        self.rssi = rssi
        self.kalmanFIlter()

    # def KalmanFilter(self):