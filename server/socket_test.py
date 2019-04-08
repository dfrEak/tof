# An example script to connect to Google using socket 
# programming in Python 
# ref: https://www.geeksforgeeks.org/socket-programming-python/

import socket # for socket 
import sys  
from time import sleep

# local file
import packet

class socket_test:
    '''
    def isAlive(s):
        try:
            if s.__socket() != None:
                return True
        except Exception:
            pass
            return False
    '''

    '''
    # default port for socket 
    port = 80
      
    try: 
        host_ip = socket.gethostbyname('www.google.com') 
    except socket.gaierror: 
      
        # this means could not resolve the host 
        print ("there was an error resolving the host")
        sys.exit() 
      
    # connecting to the server (google)
    s.connect((host_ip, port)) 
     
    print ("the socket has successfully connected to google on port == %s" %(host_ip))
    '''
    host_ip='192.168.1.178'
    port=12345
    global s
    
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as err:
            print("socket creation failed with error %s" %(err))

    def connect(self):
        self.s.connect((self.host_ip, self.port))
        print("the socket has successfully connected to %s on port %s" %(host_ip,port))
        print("this raspberry ip ",socket.gethostbyname(socket.gethostname()))
        #s.send(("try to connect").encode('utf-8'))

    def send(xshut,range):
        #s.send(("3540").encode('utf-8'))
        s.send((packet.encoding_package(
            socket.gethostbyname(socket.gethostname())
            ,xshut
            ,range)
            ).encode('utf-8'))
        print("packet xshut=%s range=%s sent" %(xshut,range))


# main
so=socket_test()
so.connect()
so.send("1","2212")
so.send("2","1432")

'''
s.send((packet.encoding_package(
    socket.gethostbyname(socket.gethostname())
    ,"1"
    ,"3312")
    ).encode('utf-8'))
    
s.send((packet.encoding_package(
    socket.gethostbyname(socket.gethostname())
    ,"2"
    ,"3312")
    ).encode('utf-8'))


while True:
    s.send((packet.encoding_package(
        socket.gethostbyname(socket.gethostname())
        ,"1"
        ,"3232")
        ).encode('utf-8'))
    sleep(5)
    s.send((packet.encoding_package(
        socket.gethostbyname(socket.gethostname())
        ,"2"
        ,"1123")
        ).encode('utf-8'))
    sleep(5)
    s.send((packet.encoding_package(
        socket.gethostbyname(socket.gethostname())
        ,"1"
        ,"2222")
        ).encode('utf-8'))
    sleep(5)
    s.send((packet.encoding_package(
        socket.gethostbyname(socket.gethostname())
        ,"2"
        ,"4213")
        ).encode('utf-8'))
    sleep(5)
    #message=s.recv(1024)
    #if (message!=b''): # for byte
    #    print (message)
    #else:
    #    break
'''

