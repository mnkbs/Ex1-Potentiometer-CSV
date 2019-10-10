

int sensorPin = A0;     
int sensorValue = 0; 
unsigned long lastReading = 0;

 
void setup() {

  Serial.begin(115200);
}
 
void loop() {
  if (millis() - lastReading >= 10) {
     sensorValue = analogRead(sensorPin);
     Serial.println(sensorValue);
     lastReading = millis();
  }
}
