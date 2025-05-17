#!/bin/python3
#coding:utf-8

import _thread
import socket
import time

def sendData(threadName, CliConnect):
    print("thread %s started"%(threadName))
    while True:
        time.sleep(1)
        try:
            data = input(">>:").strip()
            if not data: continue
            CliConnect.send(data.encode())
        except:
            print("client error")
            break
    CliConnect.close()

def recvData(threadName, CliConnect):
    print("thread %s started"%(threadName))
    while True:
        try:
            data = CliConnect.recv(1024);
            if not data: break
            print("From server: " + data.decode())
        except:
            break
    CliConnect.close()



    # msg=input('>>:').strip()
    # if not msg:continue

if __name__ == "__main__":
    coon = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    coon.connect(('127.0.0.1',8080))

    try:
        _thread.start_new_thread( recvData, ("Thread-read", coon) )
        _thread.start_new_thread( sendData, ("Thread-write", coon) )
    except:
        print("Thread start faile")

    while True:
        pass