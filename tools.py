# ref: https://www.raspberrypi-spy.co.uk/2012/06/finding-the-mac-address-of-a-raspberry-pi/

class tools:

    def __init__(self):
        pass
    
    @staticmethod
    def getEthName():
        # Get name of the Ethernet interface
        try:
            for root, dirs, files in os.walk('/sys/class/net'):
                for dir in dirs:
                    if dir[:3] == 'enx' or dir[:3] == 'eth':
                        interface = dir
        except:
            interface = "None"
        return interface
    
    @staticmethod
    def getMAC(interface='wlan0'):
        # Return the MAC address of the specified interface
        # interface = eth0 or wlan0
        try:
            str = open('/sys/class/net/%s/address' % interface).read()
        except:
            str = "00:00:00:00:00:00"
        return str[0:17]

if __name__ == "__main__":
    print(tools.getEthName())
    print(tools.getMAC('eth0'))
    print(tools.getMAC('wlan0'))