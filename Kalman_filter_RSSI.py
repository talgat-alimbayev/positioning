import numpy as np

class Kalman_filter_RSSI:
    Q = 22  # found experimentally, check Variance.py and references above for more info
    R = 0.5  # middle ground between being sluggish and too noisy
    # R = 1 # try this model noise covariance if the model is too slow to respond to the tracker movement
    def __init__(self, rssi_meas, deviceName, beacon):

        self.deviceName = deviceName
        self.beacon = beacon
        self.rssi_meas = rssi_meas # rssi measurement is initialized as rssi at 1m
        self.rssi_pred = rssi_meas
        self.rssi_est = rssi_meas
        self.sigma_est = 0  #covariance of estimation
        self.sigma_pred = 0 #covariance of prediction
        self.K = 0 #kalman gain


    def getRssiEst(self):
        return self.rssi_est

    def getQ(self):
        return Kalman_filter_RSSI.Q

    def getR(self):
        return Kalman_filter_RSSI.R

    def setRssi(self, rssi_meas):
        self.rssi_meas = rssi_meas

    def kalmanFilter(self):
        self.rssi_pred = self.rssi_est
        self.sigma_pred = self.sigma_est + Kalman_filter_RSSI.R
        self.K = self.sigma_pred / (self.sigma_pred + Kalman_filter_RSSI.Q)
        self.rssi_est = self.rssi_pred + self.K * ( self.rssi_meas - self.rssi_pred )
        self.sigma_est = self.sigma_pred - self.K * self.sigma_pred