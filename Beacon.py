import numpy as np

class Beacon:
    #https://www.wouterbulten.nl/blog/tech/kalman-filters-explained-removing-noise-from-rssi-signals/
    #https://www.sciencebuddies.org/science-fair-projects/science-fair/variance-and-standard-deviation
    #https://www.statisticshowto.com/probability-and-statistics/descriptive-statistics/sample-variance/
    Q = 22  # found experimentally, check Variance.py and references above for more info
    R = Q / 2  # I don't know how reasonable this is. This is a process noise, i.e how uncertain our
    # assumption of having no movement when in reality we might have some
    def __init__(self, id, rssi_meas, x, y, rssi_1m, N):

        self.id = id
        self.rssi_meas = rssi_meas
        self.x = x
        self.y = y
        self.rssi_1m = rssi_1m #RSSI at one meter distance, needs to be calibrated for each beacon
        self.N = N #N is a path loss coefficient. The more obstacles there are, the larger it will be
        self.d = 10 ** ( (rssi_1m - rssi) / (10*N) )

        self.rssi_est = self.rssi_1m
        self.rssi_pred = 0
        self.sigma_est = 0  #covariance of estimation
        self.sigma_pred = 0 #covariance of prediction
        self.K = 0 #kalman gain

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDistance(self):
        return self.d

    def getN(self):
        return self.N

    def setRssi(self, rssi_meas):
        self.rssi_meas = rssi_meas

    def KalmanFilter(self):
        self.rssi_pred = self.rssi_est
        self.sigma_pred = self.sigma_est + Beacon.R
        self.K = self.sigma_pred / (self.sigma_pred + Beacon.Q)
        self.rssi_est = self.rssi_pred + self.K * ( self.rssi_meas - self.rssi_pred )
        self.sigma_est = self.sigma_pred - self.K * self.sigma_pred

    def calculateDistance(self):
        self.d = 10 ** ((self.rssi_1m - self.rssi_est) / (10 * N))