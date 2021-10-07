import os

def variance(dir):
    list = os.listdir(dir)
    N = len(list) #number of samples to calculate variance
    for i in range(3):
        os.path.join(dir,list[i])
        f = open( os.path.join(dir, list[i]), "r")
        print(f.read())
    print(list[0])
