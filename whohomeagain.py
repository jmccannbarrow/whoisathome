
import datetime
from twilio.rest import Client
import json
from wia import Wia
import bluetooth
import mysql.connector
from sense_hat import SenseHat
sense = SenseHat()


account_sid = 'AC36ac6c1777bf527f2968c401d1118457'
auth_token = 'f4d63d14fa37afbc3fa1c908cc55398f'
client = Client(account_sid, auth_token)




wia = Wia()
wia.access_token = "d_sk_3HzhRkBfOYVoxjp7Yo8myN14"




while True:
   for event in sense.stick.get_events():
    if event.action == "pressed" and event.direction== "middle":
         	

         wia.Event.publish(name="button", data="Hi there")


################################################################################################
         def Authenticate(addr):
	 #Return the user of the device from the database

             mydb = mysql.connector.connect(
               host="127.0.0.1",
               user="root",
               passwd="Liverpool2020!",
               database="whoisathome"
               )

             mycursor = mydb.cursor()
             deviceId = (addr, )

             sql = "SELECT User FROM tbl_deviceusers WHERE DeviceID = %s"
             mycursor.execute(sql, deviceId)
             myresult = mycursor.fetchone()
             if mycursor.rowcount == 0:
               return ""
             else:
               for x in myresult:
                 mycursor.close()
                 return str(x)

##################################################################################################

         def CheckStatusExists(addr):
         #Check if the user of the device has an entry in the status log. 
	 #This is needed as a first-time user will not have an existing entry to reverse. 

             mydb = mysql.connector.connect(
               host="127.0.0.1",
               user="root",
               passwd="Liverpool2020!",
               database="whoisathome"
               )

             mycursor = mydb.cursor()
             deviceId = (addr, )

             sql = "SELECT DeviceID FROM tbl_statuslog WHERE DeviceID = %s"
             mycursor.execute(sql, deviceId)
             myresult = mycursor.fetchall()
             if mycursor.rowcount == 0:
               return 0
             else:
               return 1

###################################################################################################


         def GetLastStatus(addr):
         #Get the most recent status of the user of the device

             mydb = mysql.connector.connect(
               host="127.0.0.1",
               user="root",
               passwd="Liverpool2020!",
               database="whoisathome"
               )

             mycursor = mydb.cursor()
             deviceId = (addr, )

             sql = "SELECT Status FROM tbl_statuslog WHERE DeviceID = %s ORDER BY statusTime DESC LIMIT 1"
             mycursor.execute(sql, deviceId)
             myresult = str(mycursor.fetchone()[0])
             return myresult
 

###################################################################################################

         def AddStatus(addr, IsAuthenticated, Status):
         #Add the new current status of the user. This will be the opposite of the existing entry. 
      

             mydb = mysql.connector.connect(
               host="127.0.0.1",
               user="root",
               passwd="Liverpool2020!",
               database="whoisathome"
               )

             mycursor = mydb.cursor()
             deviceId = str(addr)

             sql = "INSERT INTO tbl_statuslog (DeviceID, User, StatusTime, Status) VALUES( %s, %s, NOW(), %s)"
             val = (deviceId, IsAuthenticated, Status )
             mycursor.execute(sql, val )
             mydb.commit()


###################################################################################################
         def GetSMSNumber(addr):
         #Get the mobile number associated with the device user as the recipient to send SMS messages to.

             mydb = mysql.connector.connect(
               host="127.0.0.1",
               user="root",
               passwd="Liverpool2020!",
               database="whoisathome"
               )

             mycursor = mydb.cursor()
             deviceId = (addr, )

             sql = "SELECT smsNo FROM tbl_deviceusers WHERE DeviceID = %s"
             mycursor.execute(sql, deviceId)
             myresult = mycursor.fetchone()
             if mycursor.rowcount == 0:
               return ""
             else:
               for x in myresult:
                 mycursor.close()
                 return str(x)
 
            
            ################################################################################################
         #Code Execution   
         print("looking for devices")
         nearby_devices = bluetooth.discover_devices(duration=5,lookup_names = True)
         print("found %d devices" % len(nearby_devices))
         for addr in nearby_devices:
             addr = nearby_devices[0][0]
             print(addr)
             IsAuthenticated = Authenticate(addr)
             if IsAuthenticated == "":
               print("Not Authenticated")
             else:
                print(IsAuthenticated + " Is Authenticated.")

                if CheckStatusExists(addr)== 0:
                   print("Not In Status Log")
                   AddStatus(addr, IsAuthenticated, "IN")
                   print("Added to status log with status of IN")
 		   
                else:
		  
                  LastStatus = GetLastStatus(addr)
                  print("Last Status " + LastStatus)  
                
                
                  if LastStatus == "IN":
                     AddStatus(addr, IsAuthenticated, "OUT")
                     print("Added to status log with status of OUT")
                     smsText = IsAuthenticated + " has left the house."
                  else:
                     AddStatus(addr, IsAuthenticated, "IN")
                     print("Added to status log with status of IN")
                     smsText = IsAuthenticated + " is home."
                     
                  smsNumber = GetSMSNumber(addr)
                  print(smsText)
                  print(smsNumber)


                  message = client.messages \
			   .create(
				body=smsText,
				from_='+14108241871',
				to=smsNumber
				)

		#print(message.sid)
                  
	




sense.clear()
