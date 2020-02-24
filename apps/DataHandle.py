import os

class DataHandle:
    GWAddr = ''
    DevAddr = 0
    FCnt = 0
    FLen = 0
    Payload = ''

    def __init__(self):
        pass

    def MsgParser(self, msg):
        bufIndex = 0

        if (len(msg) %2 ) !=0 :
            msg = msg[: -1]

        #self.

        bytestr = bytes.fromhex(msg)

        bufIndex += 1
        self.DevAddr = bytestr[bufIndex]

        self.GWAddr = str(bytestr[bufIndex+3]) + '.' + str(bytestr[bufIndex+2]) + '.' + str(bytestr[bufIndex+1]) + '.0'
        bufIndex+=3

        #self.Fctl
        bufIndex+=1

        #self.FCnt = int(bytestr[bufIndex+1] | (bytestr[bufIndex+2] << 8))
        bufIndex+=2

        self.FLen = int(bytestr[bufIndex+1])
        bufIndex+=1


        #self.FPort
        bufIndex+=1

        msglen = len(bytestr)


        if(self.FLen != (msglen-(bufIndex+1))):
            self.Payload = 'PayloadError'
            return

        self.Payload = ''
        for i in range (bufIndex+1, msglen):
            self.Payload += chr(bytestr[i])
        

_datahandle = DataHandle()

while 1: 
    if(os.stat('/opt/mgateway/apps/rawData.csv').st_size!=0):
        with open('/opt/mgateway/apps/rawData.csv', 'r') as fin:
            data = fin.read().splitlines(True)

            if len(data[0]) > 10 :
                _datahandle.MsgParser(data[0])
                if(_datahandle.GWAddr == "255.255.255.0"):
                    with open('/opt/mgateway/apps/parsedData.csv', 'a') as fout:
                        fout.writelines(_datahandle.GWAddr + ',' + str(_datahandle.DevAddr) + ',' + _datahandle.Payload + '\n')
                        _datahandle.Payload = ''
                
        
        with open('/opt/mgateway/apps/rawData.csv', 'w') as fout:
            fout.writelines(data[1:])