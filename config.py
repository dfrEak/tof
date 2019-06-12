#ref
#https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

import configparser
from pathlib import Path
#import os

class config:

    # parameter
    config = configparser.ConfigParser()

    # using path
    #configFile = Path(__file__).parent / "conf.ini"
    #print(configFile)

    # if using os
    #print(os.path.dirname(os.path.abspath(__file__)))

    config.read(Path(__file__).parent / "conf.ini")



if __name__ == "__main__":
    print(config.config['PEAK']['THRESHOLD'])
    print(config.config['SENSORS']['SHUTX_PIN'])
    print(type(config.config['SENSORS']['SHUTX_PIN']))

    import json
    print(json.loads(config.config['SENSORS']['SHUTX_PIN']))