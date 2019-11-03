
int sensorPin = A0;
int sensorValue = 0;
unsigned long lastReading = 0;
byte startByte = 0b00111010;
byte b[4];

void setup() {

  Serial.begin(115200);
  pinMode(sensorPin, INPUT_PULLUP);
}

void loop() {
  
if (millis() - lastReading >= 100) {
    sensorValue = analogRead(sensorPin);
    Serial.write(startByte);
    Serial.write((sensorValue >> 8) & 0xFF);
    Serial.write(sensorValue & 0xFF);

    for (int i=0; i<4; i++)
    {
       b[i]=((millis()>>(i*8)) & 0xff); 
       Serial.write(b[i]);
       lastReading = millis();
    }
 }
}
