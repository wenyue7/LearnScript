#!/bin/python3
#coding:utf-8
# 程序来源：https://blog.csdn.net/sinat_29214327/article/details/80574955

import _thread
import socket
import time

def sendData(threadName, CliConnect):
    print("thread %s started"%(threadName))
    while True:
        time.sleep(1)
        try:
            data = "test\n";
            CliConnect.send(data.encode())
        except:
            break
    CliConnect.close()

def recvData(threadName, CliConnect):
    print("thread %s started"%(threadName))
    while True:
        try:
            data = CliConnect.recv(1024);
            if not data: break
            print("From client: " + data.decode())
        except:
            break
    CliConnect.close()


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)

    print("waiting connect ...")
    while True:
        coon,client_addr=server.accept()
        try:
            _thread.start_new_thread( recvData, ("Thread-read", coon) )
            _thread.start_new_thread( sendData, ("Thread-write", coon) )
        except:
            print("Thread start faile")
            break
    server.close()