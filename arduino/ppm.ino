/* Sweep
 by BARRAGAN <http://barraganstudio.com> 
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://arduino.cc/en/Tutorial/Sweep
*/ 

#include <Servo.h> 
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
 
Servo myservo;  // create servo object to control a servo 

void setup() { 
  Serial.begin(9600);
  mySerial.begin(9600);
  myservo.attach(9);
  myservo.write(10);
  mySerial.println("start");
} 
 
void loop() { 
  if (mySerial.available()) {
    int level = mySerial.parseInt();
    mySerial.println(level);
    Serial.println(level);
    myservo.write(level);
  }
} 

