import os
import time
import socket

class PCconnection:
        def __init__(self): 
                self.host = '202.191.56.103' 
                self.port = 5540 
                self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                self.s.connect((self.host,self.port)) 
                print("Connected") 
        def send_Data(self, msg): 
                self.s.send(msg.encode())
                time.sleep(1)

myCon = PCconnection()

while 1: 
    if(os.stat('/opt/mgateway/apps/parsedData.csv').st_size!=0):
        with open('/opt/mgateway/apps/parsedData.csv', 'r') as fin:
            data = fin.read().splitlines(True)
            myCon.send_Data(data[0])
            print('Send Data to Server\n')

        with open('/opt/mgateway/apps/parsedData.csv', 'w') as fout:
            fout.writelines(data[1:])
