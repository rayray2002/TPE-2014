#include <Wire.h>
#include <Servo.h> 

Servo myservo;

int level;

void setup() {
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(9600);  // start serial for output
  myservo.attach(9);
  myservo.write(10);
}

void loop() {
  Wire.requestFrom(2, 1);    // request 6 bytes from slave device #2
  
  while (Wire.available()) {
    level = Wire.read();
    Serial.println(level); // print the character
    myservo.write(level);
  }
  if (level > 80) {
    Wire.beginTransmission(2);
    Wire.write(1);
    Wire.endTransmission();
  }
  else{
    Wire.beginTransmission(2);
    Wire.write(0);
    Wire.endTransmission();
  }
}
