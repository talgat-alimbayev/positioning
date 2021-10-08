import os
import json

def variance(dir):
    list = os.listdir(dir)
    N = len(list) #number of samples to calculate variance
    sum = 0.0
    for i in range(N):
        os.path.join(dir,list[i])
        f = open( os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)
        x = data['beacons']['ab8190d5d11e4941acc4ac233f5b8a0427114cb9']
        sum = sum + x
    mean = sum/N

    #calculating variance for a finite sample of measurements
    variance = 0
    for i in range(N):
        os.path.join(dir,list[i])
        f = open( os.path.join(dir, list[i]), "r")
        d = f.read()
        data = json.loads(d)
        x = data['beacons']['ab8190d5d11e4941acc4ac233f5b8a0427114cb9']
        variance = variance + ( x-mean )**2
    variance = variance / (N-1)
    print("mean: ", mean)
    print("variance: ", variance)

if __name__ == '__main__':
    #Just put r before your normal string it converts normal string to raw string:
    variance(r'C:\Users\tyalimbayev\Desktop\Code\positioning\venv\logs\1_centerOfTheRoom')