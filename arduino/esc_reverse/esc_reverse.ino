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
  Serial.begin(38400);
  
  Serial.println("#1 power up ESC now - stick low");
  writeAll(1000);
  delay(3000);
  Serial.println("#2 stick high");
  writeAll(2000);
  delay(1200);
  Serial.println("#3 sitck low");
  writeAll(1000);
  delay(1200);
  Serial.println("#4 middle ");
  writeAll(1500);
  delay(2500); //hear 3 beeps to enter RC neturel mode

} 
void writeAll(int s) {
  //servos[0].writeMicroseconds(s); //LU
  //servos[1].writeMicroseconds(s); //RU
  //servos[2].writeMicroseconds(s); //L
  servos[3].writeMicroseconds(s); //R
} 
void writeMicroseconds(int s) {
  //servos[0].writeMicroseconds(1500 + s); //LU
  //servos[1].writeMicroseconds(1500 - s); //RU
  //servos[2].writeMicroseconds(1500 - s); //L
  servos[3].writeMicroseconds(1500 - s); //R
}

void loop() 
{
 Serial.println("forward"); 
 writeMicroseconds(120); //forward (down,  forward)
 delay(5000);
 Serial.println("stop"); 
 writeMicroseconds(0);
 delay(5000);
  /*
  writeMicroseconds(1430); //backward
  delay(5000);
  writeMicroseconds(1500);
  delay(500);
  */
} 
