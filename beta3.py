# RPi
import time
import paho.mqtt.client as mqtt
import sys
import urllib2
# Enter Your API key here
myAPI = '10QFJTA1UGI77J7A' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
global ab,ac,ad,ae,af,ag,ah,ai
def on_connect(client, userdata, flags, rc):
    if rc==0:
       print("Connected with result code " + str(rc))
       print("connected OK")
       for i in range(1,9):
           client.subscribe("/esp8266/temp"+str(i))
    else:
        print("Bad connection Returned code=",rc)
# The callback for when a PUBLISH message is received from the server. 
def on_message(client, userdata, msg): 
    print(msg.topic+" "+str( msg.payload)) 
   # Check if this is a message for the Pi LED. 
    if msg.topic == '/esp8266/temp2': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 2 is: "+str(msg.payload))
        global ac
        ac=int(msg.payload)
        print ac
    if msg.topic == '/esp8266/temp3': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 3 is: "+str(msg.payload))
        global ad
        ad=int(msg.payload)
        print ad
    if msg.topic == '/esp8266/temp1': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 1 is: "+str(msg.payload))
        global ab
        ab=int(msg.payload)
        print ab
    if msg.topic == '/esp8266/temp4': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 4 is: "+str(msg.payload))
        global ae
        ae=int(msg.payload)
        print ae
    if msg.topic == '/esp8266/temp5': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 5 is: "+str(msg.payload))
        global af
        af=int(msg.payload)
        print af
    if msg.topic == '/esp8266/temp6': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 6 is: "+str(msg.payload))
        global ag
        ag=int(msg.payload)
        print ag
    if msg.topic == '/esp8266/temp7': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 7 is: "+str(msg.payload))
        global ah
        ah=int(msg.payload)
        print ah
    if msg.topic == '/esp8266/temp8': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 8 is: "+str(msg.payload))
        global ai
        ai=int(msg.payload)
        print ai        
# Create MQTT client and connect to localhost, i.e. the Raspberry Pi running 
# this script and the MQTT server. 
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
ab=0
ac=0
ad=0
ae=0
af=0
ag=0
ah=0
ai=0
# Connect to the MQTT server and process messages in a background thread. 
try:
    client.loop_start()
    print("Connecting to broker")
    client.connect('localhost', 1883, 60)     #connect to broker
    while 1:
        # Sending the data to thingspeak
        global ab,ac,ad,ae,af,ag,ah,ai
        conn = urllib2.urlopen(baseURL+'&field1='+str(ab)+'&field2='+str(ac)+'&field3='+str(ad)+'&field4='+str(ae)+'&field5='+str(af)+'&field6='+str(ag)+'&field7='+str(ah)+'&field8='+str(ai))
        print conn.read()
        # Closing the connection
        conn.close()
        time.sleep(5)
    #while not client.connected_flag: #wait in loop
     #   print(".")
    #  time.sleep(1)
    print("in Main Loop")
except KeyboardInterrupt:
    client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect

