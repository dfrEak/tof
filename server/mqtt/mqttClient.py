#ref: https://www.baldengineer.com/mqtt-tutorial.html
#http://www.steves-internet-guide.com/into-mqtt-python-client/

# import config
import sys
sys.path.append('../../')
from config import config

import paho.mqtt.client as mqtt
#import threading

class mqttClient:

    def __init__(self, topic):
        # parameter
        self.hostname = config.config['MQTT']['hostname']

        # file settings
        self.fileSet = config.config['MQTT']['save_file']
        self.fileName = config.config['MQTT']['save_file_name']

        # update topic
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

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        #print(self.topic)
        client.subscribe(self.topic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

        # want to save or not
        if(self.fileSet=="1"): # from conf.ini
            self.saveMessage(self.fileName, msg.payload.decode())
        elif(self.fileSet=="2"):
            self.saveMessage(msg.topic.replace(":","").replace("/","_"), msg.payload.decode())


    def start(self):
        self.client.loop_forever()

    def setTopic(self,topic):
        self.topic = topic

    # writing to file
    def saveMessage(self, fileName, message):
        print("save")
        # a for append only
        # a+ for append, read
        #print(fileName)
        self.fileHandler = open(fileName+".txt","a+")
        self.fileHandler.write(message+"\n")
        # for printing, can use flush/close too
        #self.fileHandler.flush()
        self.fileHandler.close()



if __name__ == "__main__":
    # test
    #m1=mqttClient("debug")

    print(config.config['MQTT']['hostname'])

    # use real topic
    topic1 = "b8:27:eb:c7:cc:12/1/TOF"
    #m = mqttClient(topic1)


    # multi topic
    m = mqttClient([("debug",1),(topic1,1)])
    m.start()