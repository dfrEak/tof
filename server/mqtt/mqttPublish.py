#ref: https://www.baldengineer.com/mqtt-tutorial.html

# import config
import sys
sys.path.append('../../')
from config import config

import paho.mqtt.publish as publish
import time
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

        # generate topic name
        self.defaultTopic = True
        self.topic = "debug"

    def send(self, message):
        if(self.defaultTopic):
            # default topic for testing
            publish.single(self.topic, message, hostname=self.hostname)
        else:
            # using formating topic
            publish.single(self.generateTopic(), message, hostname=self.hostname)
        print("send "+message)

    def generateTopic(self):
        # format topic <mac address>/<sensor no>/<sensor name>
        retval = ""
        mac = tools.getMAC()
        retval = mac + self.topicSeparator + self.topicSensorNo + self.topicSeparator + self.topicSensorName
        return retval

    def generateMessage(self, range, separator=" "):
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
    publish.single("debug", "0", hostname=hostname)
    time.sleep(1)
    print("Sending 1...")
    publish.single("debug", "1", hostname=hostname)

    m=mqttPublish()
    m.send("lalalaa")

    t=m.generateMessage(["123", "456", "789"])
    print(t)
    print(m.degenerateMessage(t))
    print(m.generateTopic())

    # using real topic
    m.defaultTopic=False
    m.send(m.generateMessage(range=["123", "456", "789"],separator=" "))