import mysql.connector
from datetime import datetime  

class db_connector:

    host="192.168.1.178"
    user="tof"
    passwd="tof"
    database="tof"

    global mydb
    global mycursor

    def __init__(self):
        pass

    def dbConnect(self):
        self.mydb = mysql.connector.connect(
          #host="localhost",
          host=self.host,
          user=self.user,
          passwd=self.passwd,
          database=self.database
        )
        print(self.mydb)

    def dbInsertData(ip, xshut, range_data):
        self.mycursor = mydb.cursor()

        # example show databases
        #mycursor.execute("SHOW DATABASES")
        #for x in mycursor:
        #  print(x)

        # insert
        str_now = datetime.now()
        #sql="INSERT INTO data (range_data,time) VALUES "
        #test query:
        #SELECT sensor.id FROM sensor RIGHT JOIN raspberry ON sensor.raspberry_id=raspberry.id WHERE raspberry.ip="192.168.1.38" AND sensor.xhut_pin=2
        sql="INSERT INTO data (sensor_id,range_data,time) SELECT sensor.id,%s,%s FROM sensor LEFT JOIN raspberry ON sensor.raspberry_id=raspberry.id WHERE raspberry.ip=%s AND sensor.xhut_pin=%s"
        val=(range_data,str_now,ip,xshut)
        self.mycursor.execute(sql,val)
        #print(sql,val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")


        
######################################################
if __name__ == "__main__":
    db=db_connector()
    db.dbConnect()



