
int sensorPin = A0;
int sensorValue = 0;
unsigned long lastReading = 0;


void setup() {

  Serial.begin(9600);
  //pinMode(sensorPin, INPUT_PULLUP);


}

void loop() {
    Serial.print(u8"\U0001F349");
//if (millis() - lastReading >= 10) {
 // sensorValue = analogRead(sensorPin);
 // Serial.println(sensorValue);
 // lastReading = millis();
// }
}
