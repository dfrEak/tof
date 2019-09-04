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

    @staticmethod
    def save(filename ,text):
        """
        save file
        ファイルを保存
        :param filename: str
            filename
            ファイルの名前
        :param text: str
            saved text
            保存したテキスト
        :return:
        """
        f= open(filename,"a", encoding="utf-8")
        f.write(text)
        print("save completed")

    @staticmethod
    def read(filename):
        """
        read file
        ファイルを読む
        :param filename: str
            filename
            ファイルの名前
        :return: str
            file text
            ファイルテキスト
        """
        retval=[]
        f= open(filename,"r", encoding="utf-8_sig")

        for line in f.readlines():
            # -1 to discard last \n
            str=line[:-1].split("\t")
            data=[str[0]]+str[1].split(" ")
            #data = [str[0]]
            #data.append(str[1].split(" "))
            retval.append(data)

        return retval


    @staticmethod
    def column(matrix, i):
        return [row[i] for row in matrix]

if __name__ == "__main__":
    print(tools.getEthName())
    print(tools.getMAC('eth0'))
    print(tools.getMAC('wlan0'))