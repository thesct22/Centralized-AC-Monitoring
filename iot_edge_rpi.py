# RPi
import time
import paho.mqtt.client as mqtt
import sys
import urllib2
# Enter Your API key here
myAPI = 'xxxxxxxxxxxxxxxxx'#enter your thingspeak api 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
global temp,hum
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
    if msg.topic == '/esp8266/temp': 
       # Look at the message data and perform the appropriate action. 
        print("temperature is: "+str(msg.payload))
        global temp
        temp=int(msg.payload)
        
    if msg.topic == '/esp8266/hum': 
       # Look at the message data and perform the appropriate action. 
        print("humidity is: "+str(msg.payload))
        global hum
        hum=int(msg.payload)
    
# Create MQTT client and connect to localhost, i.e. the Raspberry Pi running 
# this script and the MQTT server. 
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
temp=0
hum=0
# Connect to the MQTT server and process messages in a background thread. 
try:
    client.loop_start()
    print("Connecting to broker")
    client.connect('localhost', 1883, 60)     #connect to broker
    while 1:
        # Sending the data to thingspeak
        global ab,ac,ad,ae,af,ag,ah,ai
        conn = urllib2.urlopen(baseURL+'&field1='+str(temp)+'&field2='+str(hum))
        print conn.read()
        # Closing the connection
        conn.close()
        time.sleep(10)
    #while not client.connected_flag: #wait in loop
     #   print(".")
    #  time.sleep(1)
    print("in Main Loop")
except KeyboardInterrupt:
    client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect
