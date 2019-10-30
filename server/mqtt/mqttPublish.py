#ref: https://www.baldengineer.com/mqtt-tutorial.html

# import config
import sys
sys.path.append('../../')
from config import config

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
import datetime
import configparser
#from datetime import datetime

from tools import tools

class mqttPublish:
    def __init__(self):
        # parameter
        self.hostname = config.config['MQTT']['hostname']
        self.topicSeparator = config.config['MQTT']['topic_separator']
        self.topicSensorNo = config.config['MQTT']['topic_sensor_number']
        self.topicSensorName = config.config['MQTT']['topic_sensor_name']
        self.messageSeparator = config.config['MQTT']['message_separator']
        self.sendByte = config.config['MQTT']['send_as_byte']

        # generate topic name
        if(int(config.config['MQTT']['topic_default'])):
            # default topic for testing
            self.topic = "debug"
        else:
            # using formating topic
            self.topic = self.generateTopic()

        self.client = mqtt.Client()
        self.client.connect(self.hostname)
        self.client.subscribe(self.hostname)

    def __del__(self):
        print("destructor")
        self.client.disconnect()

    def changeTopic(self, newTopic):
        self.client.unsubscribe(self.topic)
        self.topic = newTopic
        self.client.subscribe(self.topic)

    def send(self, message):
        try:
            if self.sendByte:
                self.client.publish(self.topic, bytearray(message))
            else:
                self.client.publish(self.topic, message)

            #print("send "+message+" to "+self.topic)
        except :
            print("failed sending message")
            print(sys.exc_info())

    def generateTopic(self):
        # format topic <mac address>/<sensor no>/<sensor name>
        retval = ""
        mac = tools.getMAC()
        retval = mac + self.topicSeparator + self.topicSensorNo + self.topicSeparator + self.topicSensorName
        return retval

    def generateMessage(self, range, separator=" "):
        if(self.sendByte):
            # All byte order is big endian
            retval = b''
            # Time (8 bytes): Multiply by 1000 and round down to the nearest millisecond
            #retval += (int(datetime.timestamp(datetime.now()) * 1000)).to_bytes(8, byteorder='big')
            retval += (int(time.time())).to_bytes(8, byteorder='big')
            # Data size (4 bytes): Number of data x 4 bytes
            retval += (len(range) * 4).to_bytes(4, byteorder='big')
            # Distance (4 bytes each)
            for x in range:
                retval += (int(x)).to_bytes(4, byteorder='big')
        else:
            # format message <range><separator>....<separator><range>
            retval = ""
            # add timestamp
            #retval += str(datetime.timestamp(datetime.now())) + " "
            for x in range:
                retval+=str(x)
                retval+=separator
            # delete last space
            retval = retval[:-1]

        return retval

    def degenerateMessage(self, message, separator=" "):
        retval = message.split(separator)
        return retval



if __name__ == "__main__":
    # parameter
    hostname = config.config['MQTT']['hostname']
    print("Sending 0...")
    #publish.single("debug", "0", hostname=hostname)
    time.sleep(1)
    print("Sending 1...")
    #publish.single("debug", "1", hostname=hostname)

    m = mqttPublish()
    m.changeTopic("debug")
    #m.send("lalalaa")
    time.sleep(1)

    msg = m.generateMessage(["123", "456", "789"])

    currenttime = int.from_bytes(msg[0:8], byteorder='big')
    datasize = int.from_bytes(msg[8:12], byteorder='big')
    distance = [int.from_bytes(msg[12 + 4 * i:12 + 4 * (i + 1)], byteorder='big') for i in range(int(datasize / 4))]
    message = str(currenttime) + " " + str(datasize) + " " + str(distance)
    print(message)

    print(bytearray(msg))

    m.send(bytearray(msg))
    #print(t)
    #print(m.degenerateMessage(t))
    #print(m.generateTopic())

    # using real topic
    #m.defaultTopic=False
    #m.send(m.generateMessage(range=["123", "456", "789"],separator=" "))


