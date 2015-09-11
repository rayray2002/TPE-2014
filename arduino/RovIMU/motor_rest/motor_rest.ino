#include <Servo.h>
Servo motor;

void setup(){
  motor.attach(3);
Serial.println("ESC calibrate start");
motor.writeMicroseconds(1000);
delay(1000);
Serial.println("ESC calibrate #2");
motor.writeMicroseconds(2000);
delay(1000);
Serial.println("ESC calibrate #3");
motor.writeMicroseconds(1000);
delay(1000);
Serial.println("ESC calibrate #4");
motor.writeMicroseconds(1500);
delay(2500); //hear 3 beeps to enter RC neturel mode 
Serial.println("ESC calibrate end");
}

void loop(){
  motor.writeMicroseconds(1800);
}

