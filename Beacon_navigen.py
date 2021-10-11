import numpy as np
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)
class Beacon_navigen(metaclass=IterRegistry):
    __metaclass__ = IterRegistry
    _registry = []
    normCoef = 0

    def __init__(self, id, x, y, rssi_1m, N):
        self._registry.append(self)

        self.id = id

        self.x = x
        self.y = y

        self.rssi_1m = rssi_1m # RSSI at one meter distance, needs to be calibrated for each beacon
        self.rssi_meas = 0  # rssi measurements are initialized as zero

        self.weight = 0 # the weight for each beacon, i.e. the contribution of each beacon to the final position

        self.N = N # N is a path loss coefficient. The more obstacles there are, the larger it will be
        self.d = 0 # distance to a beacon is initialized as zero

    def getID(self):
        return self.id

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDistance(self):
        return self.d

    def getN(self):
        return self.N

    def getRSSI(self):
        return self.rssi_meas

    def getWeight(self):
        return self.weight

    @classmethod
    def getNormCoef(cls):
        return Beacon_navigen.normCoef

    def setRssi(self, rssi_meas):
        self.rssi_meas = rssi_meas

    def setWeight(self, weight):
        self.weight = weight

    @classmethod
    def setNormCoef(cls, coefficient):
        Beacon_navigen.normCoef = coefficient

    def calculateDistance(self):
        self.d = 10 ** ((self.rssi_1m - self.rssi_meas) / (10 * self.N))