import numpy as np

class Tracker_KUIS:
    #https://www.kalmanfilter.net/covextrap.html
    #https://www.wouterbulten.nl/blog/tech/kalman-filters-explained-removing-noise-from-rssi-signals/
    #https://www.sciencebuddies.org/science-fair-projects/science-fair/variance-and-standard-deviation
    #https://www.statisticshowto.com/probability-and-statistics/descriptive-statistics/sample-variance/
    Q = np.array([[1, 0], [0, 1]])  # sensor variance, needs to be obtained numerically for each tracker manufacturer

    R = np.array([[1, 0], [0, 1]])  # process noise,needs to be obtained numerically for each tracker manufacturer
    def __init__(self, id, lat, long):
        R is dependent on the time difference between GPS signals
        self.id = id
        self.coord_meas = np.array([lat, long])
        self.coord_est = np.array([51.169392, 71.449074]) #estimated coordinates, these will be returned.
        # The filter is initialized with coordinates of Astana
        self.coord_pred = np.array([51.169392, 71.449074]) #predicted coordinates
        self.sigma_est = np.array([[0, 0], [0, 0]])  #covariance of estimation
        self.sigma_pred = np.array([[0, 0], [0, 0]]) #covariance of prediction
        self.K = np.array([[0, 0], [0, 0]])  # kalman gain



    def getLat(self):
        return self.coord_est[0]

    def getLong(self):
        return self.coord_est[1]

    def KalmanFilter(self):
        self.rssi_pred = self.rssi_est
        self.sigma_pred = self.sigma_est + Beacon_kalman.R
        self.K = self.sigma_pred / (self.sigma_pred + Beacon_kalman.Q)
        self.rssi_est = self.rssi_pred + self.K * ( self.rssi_meas - self.rssi_pred )
        self.sigma_est = self.sigma_pred - self.K * self.sigma_pred
