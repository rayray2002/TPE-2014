/* Sweep
 by BARRAGAN <http://barraganstudio.com> 
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://arduino.cc/en/Tutorial/Sweep
*/ 

#include <Servo.h> 
 
Servo servos[4];  // create servo object to control a servo 
                // twelve servo objects can be created on most boards
 
int pos = 0;    // variable to store the servo position 
int s = 1500;
void setup() 
{ 
  servos[0].attach(3);  // attaches the servo on pin 9 to the servo object 
  servos[1].attach(5);  // attaches the servo on pin 9 to the servo object 
  servos[2].attach(6);  // attaches the servo on pin 9 to the servo object 
  servos[3].attach(9);  // attaches the servo on pin 9 to the servo object 
  Serial.begin(9600);
  
  writeMicroseconds(1000);
  delay(1000);
  writeMicroseconds(2000);
  delay(1000);
  writeMicroseconds(1000);
  delay(1000);
  writeMicroseconds(1500);
  delay(2500); //hear 3 beeps to enter RC neturel mode

} 
 
void writeMicroseconds(int s) {
  servos[0].writeMicroseconds(s);
  servos[1].writeMicroseconds(s);
  servos[2].writeMicroseconds(s);
  servos[3].writeMicroseconds(s);
}

void loop() 
{ 
  writeMicroseconds(1560); //forward
  delay(5000);
  writeMicroseconds(1500);
  delay(500);
  writeMicroseconds(1440); //backward
  delay(5000);
  writeMicroseconds(1500);
  delay(500);

} 
