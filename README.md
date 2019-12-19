# whoisathome
Networking for Connected Devices Assignment

Video URL - https://youtu.be/WUFSqo_syLc

The scope of this project was to develop a smart home IOT application that records the coming and goings of family members from home using Bluetooth technology in conjunction with the raspberry pi. 
It began with the concept of using fibit watches along with mobile phone devices but after many many hours of fruitless testing, it was discovered that the Bluetooth capability of the fitbit watch was unreliable for this project given the timeframe in which it had to be completed. (but is an avenue that cold be explored in future!)
A dbserver and webserver were installed on the raspberry pi and a database was set up to include a table that stored the mac addresses and details of both my phone and my wife Daire’s phone. This database also included a table that stored details of ins and outs of the home.
Upon entering the house, whoever is home would press a button on the sensehat of the raspberry pi and the pi would then firstly check for Bluetooth devices and then check the database for details of the Bluetooth device present. It would then post details of the in or out status of relevant person and post it to a website which displayed these details in real time on my local machine.
An sms message is then sent to the other person in db to inform them of activity in the house, whether the other person is in/out etc.
IoT platform WIA is also used to send a tweet to a twitter account when there is activity in the house.
If time had allowed, the project could be expanded to host the local site and chart various trends of ins/outs over time.
