#include <Servo.h> 
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
 
Servo r_motor;
Servo l_motor;

int level = 1531;
int dir;
int l_level = 0;
int r_level = 0;
int value;

void setup() { 
  Serial.begin(9600);
  mySerial.begin(9600);
  r_motor.attach(6);
  l_motor.attach(5);
  //mySerial.println("start");
  Serial.println("start");
} 

void loop() { 
  if (mySerial.available()) {
    value = mySerial.read();
    
    mySerial.println(value);
    if (dir != value) {
      dir = value;
      Serial.print(value);
      Serial.print(" ");
      Serial.print(dir);
      Serial.print(" ");
      Serial.print(l_level);
      Serial.print(" ");
      Serial.println(r_level);
    }
  }
  
  
  if (dir == '1') {
    l_motor.writeMicroseconds(l_level + level);
    r_motor.writeMicroseconds(r_level + level);
    delay(1000);
  }
  else if (dir == '2') {
    r_motor.writeMicroseconds(level);
    delay(1000);
  }
  else if (dir == '3') {
    l_motor.writeMicroseconds(level);
    delay(1000);
  }
  if (dir == '4') {
    l_motor.writeMicroseconds(1466 - l_level);
    r_motor.writeMicroseconds(1466 - r_level);
    delay(1000);
  }
  else {
    l_motor.writeMicroseconds(1500);
    r_motor.writeMicroseconds(1500);
  }
  if (dir == '5') {
    l_level++;
    r_level++;
  }
  if (dir == '6') {
    l_level--;
    r_level--;
    if (l_level < 0) {
      l_level = 0;
    }
    if (r_level < 0) {
      r_level = 0;
    }
  }
  if (dir == '7') {
    l_level++;
  }
  if (dir == '8') {
    r_level++;
  }
  
  dir = 0;
}













  /*

  if (dir == 2 or dir == 3 or dir == 1) {
    for (int i = 0; i<11; i++) {
      if (l_time > i) {
        l_motor.writeMicroseconds(level);
      }
      else{
        l_motor.writeMicroseconds(1500);
      }
      if (r_time > i) {
        r_motor.writeMicroseconds(level);
      }
      else{
        r_motor.writeMicroseconds(1500);
      }
      delay(100);
    }
  }
  
  if (dir == 0) {
    r_time = 0;
    l_time = 0;
    r_motor.writeMicroseconds(1500);
    l_motor.writeMicroseconds(1500);
  }
  
  if (dir == 4) {
    r_motor.writeMicroseconds(1400);
    l_motor.writeMicroseconds(1400);
    delay(400);
    r_motor.writeMicroseconds(1500);
    l_motor.writeMicroseconds(1500);
    delay(600);
  }
  */
  
