#ref: https://www.baldengineer.com/mqtt-tutorial.html
#http://www.steves-internet-guide.com/into-mqtt-python-client/

# import config
import sys
sys.path.append('../../')
from config import config
from pathlib import Path
import os
import time
import datetime


import paho.mqtt.client as mqtt
#import threading

class mqttClient:

    def __init__(self, topic="debug"):
        # parameter
        self.hostname = config.config['MQTT']['hostname']

        # file settings
        self.fileSet = config.config['MQTT']['save_file']
        self.fileFolder = Path(config.config['MQTT']['save_file_folder'])
        self.fileName = config.config['MQTT']['save_file_name']
        self.saveTime = int(config.config['MQTT']['save_time'])
        self.maxFileSize = int(config.config['MQTT']['max_file_size'])
        self.sendByte = config.config['MQTT']['send_as_byte']

        # update topicasd
        self.topic = topic

        # initialize the mqtt client
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        #client.connect("iot.eclipse.org", 1883, 60)
        self.client.connect("localhost", 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        print("loop")
        #client.loop_start()

    def __del__(self):
        print("destructor")
        #self.fileHandler.close()
        self.client.disconnect()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        #print(self.topic)
        client.subscribe(self.topic)
        #print(self.fileFolder)
        #print(self.fileSet)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        # want to save or not
        if(self.fileSet=="1"): # from conf.ini
            self.saveMessage(self.fileName, msg.payload)
        elif(self.fileSet=="2"):
            self.saveMessage(msg.topic.replace(":","").replace("/","_"), msg.payload)
        elif(self.fileSet=="3"):
            self.saveMessage(msg.topic.replace(":","").replace("/","_") +"_"+ datetime.date.today().strftime("%Y%m%d"), msg.payload)


    def start(self):
        self.client.loop_forever()

    def setTopic(self,topic):
        self.topic = topic

    def encodeMessage(self, msg):
        if(self.sendByte):
            currenttime = int.from_bytes(msg[0:8], byteorder='big')
            datasize = int.from_bytes(msg[8:12], byteorder='big')
            distance = [int.from_bytes(msg[12 + 4 * i:12 + 4 * (i + 1)], byteorder='big') for i in range(int(datasize / 4))]
            message = str(currenttime)+" "+str(datasize)+" "+str(distance)
        else:
            message = msg.decode()
            if(self.saveTime==1):
                message=str(time.time())+"\t"+message
            elif(self.saveTime==2):
                message=str(datetime.datetime.now().strftime("%H:%M:%S.%f"))+"\t"+message

        print(message)
        return message

    # writing to file
    def saveMessage(self, fileName, msg):
        #print("save")
        # a for append only
        # a+ for append, read
        #print(self.fileFolder / (fileName+".txt"))

        # checking file size
        self.checkFile((self.fileFolder / (fileName+".txt")).as_posix())

        self.fileHandler = open((self.fileFolder / (fileName+".txt")).as_posix(),"a+")
        #self.fileHandler = open((fileName+".txt"),"a+")

        message = self.encodeMessage(msg)

        self.fileHandler.write(message+"\n")
        # for printing, can use flush/close too
        #self.fileHandler.flush()
        self.fileHandler.close()



    def checkFile(self,filePath):
        if(os.path.isfile(filePath)):
            #if more than max file size in MB
            if(os.path.getsize(filePath)>(self.maxFileSize*1024*1024)):
                os.rename(filePath,filePath[:-4]+"_"+str(int(time.time()))+".txt")


if __name__ == "__main__":
    # test
    #m1=mqttClient("debug")

    print(config.config['MQTT']['hostname'])

    # use real topic
    topic1 = "b8:27:eb:c7:cc:12/1/TOF"
    #m = mqttClient(topic1)

    # checking file size
    #print(os.path.getsize("C:\\Users\\eric\\Dropbox\\s2\\thesis\\rashberry pi\\people detection\\server\\mqtt\\debug.txt"))

    # multi topic
    m = mqttClient([("debug",1),(topic1,1)])
    m.start()