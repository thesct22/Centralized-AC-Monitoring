#include <ESP8266WiFi.h>
#include <PubSubClient.h>

char* ssid = "dummy";
char* password = "lmfaohaha";
char* mqtt_server = "192.168.137.128";
WiFiClient espClient;
PubSubClient client(espClient);
long now = millis();
long lastMeasure = 0;
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi connected - ESP IP address: ");
  Serial.println(WiFi.localIP());
}
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
     /*
     YOU  NEED TO CHANGE THIS NEXT LINE, IF YOU'RE HAVING PROBLEMS WITH MQTT MULTIPLE CONNECTIONS
     To change the ESP device ID, you will have to give a unique name to the ESP8266.
     Here's how it looks like now:
       if (client.connect("ESP8266Client")) {
     If you want more devices connected to the MQTT broker, you can do it like this:
       if (client.connect("ESPOffice")) {
     Then, for the other ESP:
       if (client.connect("ESPGarage")) {
      That should solve your MQTT multiple connections problem

     THE SECTION IN loop() function should match your device name
    */
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");  
      // Subscribe or resubscribe to a topic
      // You can subscribe to more topics (to control more LEDs in this example)
      client.subscribe("esp8266/4");
      client.subscribe("esp8266/5");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void setup() {
  Serial.begin(115200);
  WiFi.hostname("SCT_MCU");
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}
float val;
long val1;
int a;
char ab[5];
void loop() {
  // put your main code here, to run repeatedly:
if (!client.connected()) {
    reconnect();
  }
  if(!client.loop())
    client.connect("ESP8266Client");
now = millis();
  // Publishes new temperature and humidity every 10 seconds
  if (now - lastMeasure > 15000) {
    lastMeasure = now;
  //val=analogRead(A0);
  //val=val*300/1024;
  val1=random(23,26);
  val=val1;
  Serial.print("value is");
  Serial.println(val);
  a=val;
  itoa(a,ab,10);
  client.publish("/esp8266/temp5", ab);
  }
}
