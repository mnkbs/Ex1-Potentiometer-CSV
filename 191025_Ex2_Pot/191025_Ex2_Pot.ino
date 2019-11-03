int sensorPin = A0;
int sensorValue = 0;
unsigned long lastReading = 0;
char buf[4];

void setup() {
  Serial.begin(115200);
  pinMode(sensorPin, INPUT_PULLUP);\
}

void loop() {
 
if (millis() - lastReading >= 100) {
    sensorValue = analogRead(sensorPin);
    sprintf (buf, "%04u", sensorValue);
    Serial.print(buf);
    lastReading = millis();
  }
}
