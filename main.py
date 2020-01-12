import matplotlib.pyplot as mpl
import random

offset = 2
arr = [0]
temp = []


all = []

def perlin():
    # value = random.randint(arr[-1]-offset, arr[-1]+offset)
    # if (value > border or value < -border):
    #     perlin()
    # else:
    #     arr.append(value)
    arr.append(random.randint(arr[-1]-offset, arr[-1]+offset))



def smooth():
    all.append([])
    for i in range(len(all[-2])-1):
        all[-1].append((all[-2][i]+all[-2][i+1])/2)


def main():
    for i in range(5000):
        perlin()

    all.append(arr)

    for j in range(2500):
        smooth()

    mpl.figure('Perlin Noise 1D')
    frame1 = mpl.gca()
    frame1.axes.xaxis.set_ticklabels([])
    mpl.plot(all[-1])
    mpl.show()
    
main()