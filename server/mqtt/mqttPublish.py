#ref: https://www.baldengineer.com/mqtt-tutorial.html

import sys
sys.path.append('../../')
import paho.mqtt.publish as publish
import time
import configparser

from tools import tools

class mqttPublish:
    def __init__(self):
        # parameter
        config = configparser.ConfigParser()
        config.read('../../conf.ini')
        self.hostname = config['MQTT']['hostname']
        self.topicSeparator = config['MQTT']['topic_separator']
        self.topicSensorNo = config['MQTT']['topic_sensor_number']
        self.topicSensorName = config['MQTT']['topic_sensor_name']
        self.messageSeparator = config['MQTT']['message_separator']

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
        for x in range:
            retval+=x
            retval+=separator
        # delete last space
        retval = retval[:-1]
        return retval

    def degenerateMessage(self, message, separator=" "):
        retval = message.split(separator)
        return retval

if __name__ == "__main__":
    # parameter
    config = configparser.ConfigParser()
    config.read('../../conf.ini')
    hostname = config['MQTT']['hostname']
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