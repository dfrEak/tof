# ref: https://www.geeksforgeeks.org/socket-programming-python/

# first of all import the library 
import socket                
import threading
import time
import sys

# local file
import packet
sys.path.append('..')
from db_mysql.db_connector import db_connector
from string_table import str_parser

class server:

    global s,port
    
    #########################################################################
    # db connection
    db=db_connector()
    # connect
    db.dbConnect()

    def __init__(self):
        #########################################################################
        # create a socket object
        self.s = socket.socket()
        print ("Socket successfully created")

        # reserve a port on your computer in our
        # case it is 12345 but it can be anything
        self.port = 12345

        # Next bind to the port
        # we have not typed any ip in the ip field
        # instead we have inputted an empty string
        # this makes the server listen to requests
        # coming from other computers on the network
        self.s.bind(('', self.port))
        print ("socket binded to %s" %(self.port))

        # put the socket into listening mode
        self.s.listen(5)      # max backlog of connections
        print ("socket is listening")
        #########################################################################
        
        # a forever loop until we interrupt it or an error occurs
        while True:

            # Establish connection with client.
            client_sock, addr = self.s.accept()
            print ('Got connection from', addr)

            # Client handler
            client_handler = threading.Thread(
                target=self.handle_client_connection,args=(client_sock,addr,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
            )
            client_handler.start()


    #ref: https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
    def handle_client_connection(client_socket,addr):
        while True:
            # get data from client
            request = client_socket.recv(1024)
            if request:
                print ('Received {}'.format(request))
                #processData(request)


        # send a thank you message to the client.
        client_socket.send(('Thank you for connecting').encode('utf-8'))
        time.sleep(5)
        client_socket.send(('ACK!').encode('utf-8'))
        # Close the connection with the client
        client_socket.close()
        print ('Close connection from', addr)


    def processData(data):
        decode=packet.decoding_package(data)
        print(decode)
        self.db.dbInsertData(decode[str_parser.IP],int(decode[str_parser.XSHUT]),int(decode[str_parser.RANGE]))



######################################################
if __name__ == "__main__":
    s=server()
    


