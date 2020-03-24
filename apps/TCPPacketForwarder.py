import os
import time
import socket
from threading import Thread
import threading
import sys

class PCconnection:
        def __init__(self): 
            self.host = '192.168.16.102' 
            self.port = 23 
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            self.s.connect((self.host,self.port)) 
            print("Connected") 

        def send_Data(self, msg): 
            self.s.send(msg.encode())
            time.sleep(1)

        def recv_Data(self, rxdata):
            rxdata = (self.s.recv(4096)).decode('utf8')
            if not rxdata: sys.exit(0)
            print(rxdata)
            with open(rxDir, 'a+') as fout:
                fout.writelines(str(rxdata))

myCon = PCconnection()

def SendThread(txDir):
    while True:
        if(os.stat(txDir).st_size!=0):
            with open(txDir, 'r') as fin:
                data = fin.read().splitlines(True)
                myCon.send_Data(data[0])
                print('Send Data to Server\n')

            with open(txDir, 'w') as fout:
                fout.writelines(data[1:])

def RecvThread(rxDir):
    while True:
        rxdata = 0
        myCon.recv_Data(rxdata)
        


txDir = './txData.csv'
rxDir = './rxData.csv'

try:
	t = time.time()
	t1 = threading.Thread(target=SendThread, args=(txDir,))
	t2 = threading.Thread(target=RecvThread, args=(rxDir,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print ("done in ", time.time()- t)
except Exception as e: print(e)
