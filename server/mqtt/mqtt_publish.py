#ref: https://www.baldengineer.com/mqtt-tutorial.html

import paho.mqtt.publish as publish
import time
import configparser

class mqtt_publish:
    def __init__(self):
        # parameter
        config = configparser.ConfigParser()
        config.read('../../conf.ini')
        self.hostname = config['MQTT']['hostname']

        # generate topic name
        self.topic = "debug"

    def send(self, message):
        publish.single(self.topic, message, hostname=self.hostname)
        print("send "+message)

    def generateMessage(self, range, separator=" "):
        retval=""
        for x in range:
            retval+=x
            retval+=separator
        # delete last space
        retval = retval[:-1]
        return retval

if __name__ == "__main__":
    print("Sending 0...")
    publish.single("debug", "0", hostname="localhost")
    time.sleep(1)
    print("Sending 1...")
    publish.single("debug", "1", hostname="localhost")

    m=mqtt_publish()
    m.send("lalalaa")

    print(m.generateMessage(["123","456","789"]))