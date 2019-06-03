#ref: https://www.baldengineer.com/mqtt-tutorial.html

import paho.mqtt.client as mqtt
import configparser

class mqttClient:

    def __init__(self, topic):
        # parameter
        config = configparser.ConfigParser()
        config.read('../../conf.ini')
        self.hostname = config['MQTT']['hostname']

        # update topic
        self.topic = topic

        # initialize the mqtt client
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        #client.connect("iot.eclipse.org", 1883, 60)
        client.connect("localhost", 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        client.subscribe(self.topic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

