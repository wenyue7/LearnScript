import os
import time
import threading
import serial
import mpty

# 需要安装 pyserial: pip install pyserial


def prnSerInfo(ser):
    print("============ Ser Info ============")
    '''
    ser.bytesize=8                #字节大小
    ser.bytesize=serial.EIGHTBITS #8位数据位
    ser.parity=serial.PARITY_EVEN  #偶校验
    ser.parity=serial.PARITY_NONE  #无校验
    ser.parity=serial.PARITY_ODD   #奇校验
    ser.stopbits=1                #停止位
    ser.timeout=0.5               #读超时设置
    ser.writeTimeout=0.5          #写超时
    ser.xonxoff                    #软件流控
    ser.rtscts                     #硬件流控
    ser.dsrdtr                     #硬件流控
    ser.interCharTimeout           #字符间隔超时
    '''
    print("ser name:         ", ser.name)         #打印设备名称
    print("ser port:         ", ser.port)         #打印设备名
    print("baudrate:         ", ser.baudrate)     #波特率
    print("bytesize:         ", ser.bytesize)     #字节大小
    print("parity:           ", ser.parity)       #校验位N－无校验，E－偶校验，O－奇校验
    print("stopbits:         ", ser.stopbits)     #停止位
    print("timeout:          ", ser.timeout)      #读超时设置
    print("writeTimeout:     ", ser.writeTimeout) #写超时
    print("xonxoff:          ", ser.xonxoff)      #软件流控
    print("rtscts:           ", ser.rtscts)       #硬件流控
    print("dsrdtr:           ", ser.dsrdtr)       #硬件流控
    print("interCharTimeout: ", ser.interCharTimeout)#字符间隔超时


def creatSer():
    mSer1 = serial.Serial(mpty.slaveName1, 38400, timeout = 0.5)
    if mSer1.isOpen():
        print("mSer1 open success !")
        prnSerInfo(mSer1)
    else:
        print("mSer1 open failed !")
        # mSer1.open() #打开端口
    # mSer1.baudrate=38400            #设置波特率

    mSer2 = serial.Serial(mpty.slaveName2, 38400, timeout = 0.5)
    if mSer2.isOpen():
        print("mSer2 open success !")
        prnSerInfo(mSer2)
    else:
        print("mSer2 open failed !")

    return mSer1, mSer2

def destroy():
    mSer1.close();
    mSer2.close();


def sendData(serial, data):
    if data != "":
        # encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。
        ret = serial.write(str(data).encode())

    return ret


def recvData(serial):
    while True:
        # encode() 方法正好相反，decode() 方法用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”。
        data = serial.readline().decode()  # 读一行，以/n结束，要是没有/n就一直读，阻塞。
        # data = serial.read_all()
        # data = ser.read(20) #是读20个字符
        # data = ser.readlines()和ser.xreadlines()#都需要设置超时时间
        if data == '':
            continue
        else:
            break
    return data




def test():
    mpty.createInteractionWithThread()
    ser1,ser2 = creatSer()

    while True:
        sendData(ser1, "hello world")
        data = recvData(ser2)
        print("---- recv data ----", data)

    destroy()


if __name__ == "__main__":
    test()
