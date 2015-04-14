#include <Servo.h> 
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
 
Servo r_motor;
Servo l_motor;

float level = 51;

void setup() { 
  Serial.begin(9600);
  mySerial.begin(9600);
  r_motor.attach(6);
  r_motor.write(10);
  l_motor.attach(5);
  l_motor.write(10);
  //mySerial.println("start");
  //Serial.println("start");
} 

void loop() { 
  if (mySerial.available()) {
    int dir = mySerial.parseInt() % 10;
    //mySerial.println(mySerial.parseInt());
    if (dir == 1) {
      r_motor.write(level);
      l_motor.write(level);
    }
    else if (dir == 2) {
      r_motor.write(0);
      l_motor.write(level);
    }
    else if (dir == 3) {
      r_motor.write(level);
      l_motor.write(0);
    }
    else if (dir == 0) {
      r_motor.write(0);
      l_motor.write(0);
    }
    if (dir == 4) {
      level += 0.3;
    }
    else if (dir == 5) {
      level -= 0.3;
    }
    if (level > 60) {
      level = 60;
    }
    if (level < 50.2) {
      level = 50.2;
    }
    Serial.println(level);
  }
}
