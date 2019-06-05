#ref: https://www.baldengineer.com/mqtt-tutorial.html
#http://www.steves-internet-guide.com/into-mqtt-python-client/

import paho.mqtt.client as mqtt
import configparser

class mqttClient:

    def __init__(self, topic):
        # parameter
        config = configparser.ConfigParser()
        config.read('../../conf.ini')
        self.hostname = config['MQTT']['hostname']

        # file settings
        self.fileSet = config['MQTT']['save_file']
        self.fileName = config['MQTT']['save_file_name']
        # a for append only
        # a+ for append, read
        self.fileHandler = open(self.fileName,"a+")

        # update topic
        self.topic = topic

        # initialize the mqtt client
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        #client.connect("iot.eclipse.org", 1883, 60)
        client.connect("localhost", 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        print("loop")
        #client.loop_start()
        client.loop_forever()

    def __del__(self):
        print("destructor")
        self.file.close()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        client.subscribe(self.topic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

        # want to save or not
        if(self.fileSet=="1"):
            self.saveMessage(msg.payload.decode())


    # writing to file
    def saveMessage(self, message):
        print("save")
        self.fileHandler.write(message+"\n")
        # for printing, can use flush/close too
        #self.fileHandler.flush()
        self.fileHandler.flush()


if __name__ == "__main__":
    # test
    #m=mqttClient("debug")

    # use real topic
    topic1 = "b8:27:eb:c7:cc:12/1/TOF"
    m = mqttClient(topic1)
