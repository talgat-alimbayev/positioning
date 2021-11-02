import numpy as np
from numpy.linalg import inv
class Tracker_KUIS:
    #initialize with the GPS measurements
    #use setMeas() and kalmanFilter() to set measurement and filter them using Kalman filter
    Q = np.array([[0.00000001, 0], [0, 0.00000001]])  # sensor variance, was calculated for gosafe trackers
    # R = np.array([[0.0000000001, 0], [0, 0.0000000001]])  # process noise
    R = np.array([[0.0000000005, 0], [0, 0.0000000005]])  # process noise
    def __init__(self, id, lat_init, long_init):
        self.id = id
        self.coord_meas = np.array([0, 0])
        self.coord_est = np.array([lat_init, long_init]) #estimated coordinates, these will be returned.
        # The filter is initialized with the current GPS coordinates as initial estimates
        self.coord_pred = np.array([lat_init, long_init]) #predicted coordinates
        self.sigma_est = np.array([[0, 0], [0, 0]])  #covariance of estimation
        self.sigma_pred = np.array([[0, 0], [0, 0]]) #covariance of prediction
        self.K = np.array([[0, 0], [0, 0]])  # kalman gain
        ### just for debugging
        self.debug = []
    def getLat(self):
        return self.coord_est[0]

    def getLong(self):
        return self.coord_est[1]

    def setMeas(self, lat, long):
        self.coord_meas = np.array([lat, long])

    def getMeas(self):
        return self.coord_meas

    def getDebug(self):
        return self.debug

    def kalmanFilter(self):
        self.coord_pred = self.coord_est
        self.sigma_pred = self.sigma_est + Tracker_KUIS.R
        self.K = self.sigma_pred @ inv(Tracker_KUIS.Q+self.sigma_pred)
        self.coord_est = self.coord_pred + self.K @ (self.coord_meas - self.coord_pred)
        self.sigma_est = (np.identity(2) - self.K) @ self.sigma_pred
        self.debug.append({"id":self.id, "lat_long_meas":self.coord_meas,
                           "lat_long_est":self.coord_est, "lat_long_pred":self.coord_pred,
                           "kalman_gain":self.K, "sigma_pred": self.sigma_pred,
                           "sigma_est":self.sigma_est})