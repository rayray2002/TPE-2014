#include <Wire.h>

void setup() {
  Serial.begin(9600);
  Wire.begin(2);                // join i2c bus with address #2
  Wire.onRequest(requestEvent); // register event
  Wire.onReceive(receiveEvent);
  pinMode(13, OUTPUT);
}

void loop() {
}

void requestEvent() {
  int level = analogRead(0) / 10 + 49;
  Wire.write(level);
}
void receiveEvent(int howmany) {
  digitalWrite(13, Wire.read());
}
