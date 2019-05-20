#ref: https://www.baldengineer.com/mqtt-tutorial.html

import paho.mqtt.publish as publish
import time
print("Sending 0...")
publish.single("debug", "0", hostname="localhost")
time.sleep(1)
print("Sending 1...")
publish.single("debug", "1", hostname="localhost")