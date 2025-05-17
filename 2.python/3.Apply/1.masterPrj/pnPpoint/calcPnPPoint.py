#! /usr/bin/python
#说明:这个程序是为了计算由世界坐标系中外参标定图纸中的网格点到世界坐标系中球面上对应的点
#    这里认为球面半径为1,这也是在下边计算scale时使用1/[]的原因,整个的原理很简单,就是三角
#    形相似
import numpy as np
import math

def inputPoint():
    rawstr = str(input("!!!Note: You neet input three number split by space!\nPlease inter [x y z]: "))
    list = rawstr.split(' ')
    rawP = np.array([float(list[0]), float(list[1]), float(list[2])], dtype=np.float)
    print("Your input data is: ", rawP)
    return rawP


def calcPnPPoint(point):
    scale = 1 / math.sqrt(point[0] * point[0] + point[1] * point[1] + point[2] * point[2])
    retdata = np.array([point[0] * scale, point[1] * scale, point[2] * scale,])
    print("result is: ", retdata)
    return retdata

# 用于计算x轴指向的标定点顺时针旋转120度之后的坐标点
def rotate120(point):
    pointTmp = np.array([point[0], point[1]])
    rotateMat = np.array([[float(-0.5), float(0.87)], [float(-0.87), float(0.5)]])
    retdata = rotateMat.dot(pointTmp)
    print("result is: ", retdata)
    return retdata

# 用于计算x轴指向的标定点顺时针旋转240度之后的坐标点
def rotate240(point):
    pointTmp = np.array([point[0], point[1]])
    rotateMat = np.array([[float(-0.5), float(-0.87)], [float(0.87), float(0.5)]])
    retdata = rotateMat.dot(pointTmp)
    print("result is: ", retdata)
    return retdata

def main():
    gridData = inputPoint()
    worldP = calcPnPPoint(gridData)
    # afterRotate = rotate120(gridData)
    # afterRotate = rotate240(gridData)

if __name__=='__main__':
    main()
