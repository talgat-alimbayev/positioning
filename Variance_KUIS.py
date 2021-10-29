import os
import json

def variance(dir, which_coordinate):
    list = os.listdir(dir)
    N = len(list) #number of samples to calculate variance
    sum = 0.0
    for i in range(N):
        f = open( os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)
        x = data["msg"]["sub_packet_1_data"]["values"][which_coordinate]
        sum = sum + x
        # print(list[i])
        # print(x)
        # print(sum)
    mean = sum/N

    #calculating variance for a finite sample of measurements
    variance = 0
    for i in range(N):
        f = open( os.path.join(dir, list[0]), "r")
        d = f.read()
        data = json.loads(d)
        x = data["msg"]["sub_packet_1_data"]["values"][which_coordinate]
        variance = variance + ( x-mean )**2
    variance = variance / (N-1)
    print(which_coordinate, "mean: ", mean)
    print(which_coordinate, "variance: ", variance)

if __name__ == '__main__':
    #Just put r before your normal string it converts normal string to raw string:
    dir = r"C:\Users\tyalimbayev\OneDrive - ТОО Кар-тел\Рабочий стол\КУИС\Logs_variance"
    variance("KUIS_logs_on_window_tracker_(used_for_variance)", "latitude")
    variance("KUIS_logs_on_window_tracker_(used_for_variance)", "longitude")