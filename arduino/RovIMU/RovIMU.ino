#include <Wire.h>
#include "I2Cdev.h"
#include "RTIMUSettings.h"
#include "RTIMU.h"
#include "RTFusionRTQF.h" 
#include "CalLib.h"
#include "Rov.h"
#include <EEPROM.h>
#include <SoftwareSerial.h>
#include <Servo.h>

RTIMU *imu;                                           // the IMU object
RTFusionRTQF fusion;                                  // the fusion object
RTIMUSettings settings;                               // the settings object
Rov rov;

//  DISPLAY_INTERVAL sets the rate at which results are displayed
#define DISPLAY_INTERVAL  100                         // interval between pose displays
#define LIGHT_PIN 13
#define CAMERA_PIN 12

SoftwareSerial mySerial(10, 11); // RX, TX

unsigned long lastDisplay;
unsigned long lastRate;
int sampleCount;

#define MOTOR_L 0
#define MOTOR_R 1
#define MOTOR_LU 2
#define MOTOR_RU 3
#define NO_SERVO 4

Servo motors[4];
int fixedServoValues[4];
boolean fixed = false;

void writeAll(int s) {
  for(int i=0; i<4; i++)
  motors[i].writeMicroseconds(s); 
}

void setupMotors() {
  motors[0].attach(6); //L
  motors[1].attach(9); //R
  motors[2].attach(3); //LU
  motors[3].attach(5); //RU
  delay(500);
  if(DEBUG) Serial.println("ESC calibrate start - stick low");
  writeAll(1000);
  delay(3000);
  if(DEBUG) Serial.println("ESC calibrate #2 - stick high");
  writeAll(2000);
  delay(1200);
  if(DEBUG) Serial.println("ESC calibrate #3 - stick low");
  writeAll(1000);
  delay(1200);
  if(DEBUG) Serial.println("ESC calibrate #4 - stick middle - long beep");
  writeAll(1500);
  delay(3000); //hear 3 beeps to enter RC neturel mode 
  if(DEBUG) Serial.println("ESC calibrate end");
}

void setup() 
{
    if(DEBUG) Serial.print("setup() #1");
    Serial.begin(SERIAL_PORT_SPEED);
    mySerial.begin(38400);
    pinMode(LIGHT_PIN, OUTPUT);
    pinMode(CAMERA_PIN, OUTPUT);
    
    setupMotors();
    rov = Rov();
    rov.init();
    
    int errcode;
    Wire.begin();
    imu = RTIMU::createIMU(&settings);                        // create the imu object
  
    if(DEBUG) Serial.print("ArduinoIMU starting using device ");
    if(DEBUG) Serial.println(imu->IMUName());
    if ((errcode = imu->IMUInit()) < 0) {
        if(DEBUG) {
            Serial.print("Failed to init IMU: "); 
            Serial.println(errcode);
        }
    }
    if (imu->getCalibrationValid())
        if(DEBUG) Serial.println("Using compass calibration");
    else
        if(DEBUG) Serial.println("No valid compass calibration data");
    // Slerp power controls the fusion and can be between 0 and 1
    // 0 means that only gyros are used, 1 means that only accels/compass are used
    // In-between gives the fusion mix.
    fusion.setSlerpPower(0.3);
    fusion.setGyroEnable(true);
    fusion.setAccelEnable(true);
    fusion.setCompassEnable(true);
    if(DEBUG) Serial.print("setup() #N");
}

void sendGyroData(RTVector3 p ) {
#ifdef EV3_COMM
    mySerial.write( 'a' );
    short x = p.x() * RTMATH_RAD_TO_DEGREE * 100;
    mySerial.write( (byte)x );
    mySerial.write( (byte)(x >> 8) );
    short y = p.y() * RTMATH_RAD_TO_DEGREE * 100;
    mySerial.write( (byte)y );
    mySerial.write( (byte)(y >> 8) );
    short z = p.z() * RTMATH_RAD_TO_DEGREE * 100;
    mySerial.write( (byte)z );
    mySerial.write( (byte)(z >> 8) );
    mySerial.write( '\n' );
#endif 
}
    
char buffer[64];
int pos = 0;
void processSerial(int index, int len) {
  char s[len+1];
  
  for(int i=0; i< len; i++)
    s[i] = buffer[i+index +1];
  s[len] = 0;
    
  Serial.print(">>");
  Serial.println(s);
  
  if( strcmp("init", s) == 0) {
  }
  else if( strcmp("camera_on", s) == 0) {
    digitalWrite(CAMERA_PIN, HIGH);
  }
  else if( strcmp("camera_off", s) == 0) {
    digitalWrite(CAMERA_PIN, LOW);
  }
  else if( strcmp("light_on", s) == 0) {
    digitalWrite(LIGHT_PIN, HIGH);
  }
  else if( strcmp("light_off", s) == 0) {
    digitalWrite(LIGHT_PIN, LOW);
  }
  else if( strcmp("forward", s) == 0) {
    rov.forward();
    fixed = true;
    fixedServoValues[MOTOR_L] = fixedServoValues[MOTOR_R] = 1500 + 100.0 * rov.power;
  }
  else if( strcmp("backward", s) == 0) {
    rov.backward();
    fixedServoValues[MOTOR_L] = fixedServoValues[MOTOR_R] = 1500 + 100.0 * rov.power;
  }
  else if( strcmp("stop", s) == 0) {
    rov.stop();
    fixed = false;
    fixedServoValues[MOTOR_L] = fixedServoValues[MOTOR_R] = 1500;
    fixedServoValues[MOTOR_LU] = fixedServoValues[MOTOR_RU] = 1500;
  }
  else if( strcmp("right", s) == 0) {
    rov.right();
    fixed = true;
    fixedServoValues[MOTOR_L] = 1500; 
    fixedServoValues[MOTOR_R] = 1600;
    
  }
  else if( strcmp("left", s) == 0) {
    rov.left();
    fixed = true;
    fixedServoValues[MOTOR_L] = 1600; 
    fixedServoValues[MOTOR_R] = 1500;
  }
  else if( strcmp("up", s) == 0) {
    rov.up();
    fixed = true;
    fixedServoValues[MOTOR_LU] = 1600; 
    fixedServoValues[MOTOR_RU] = 1600;
    }
  else if( strcmp("down", s) == 0) {
    rov.down();
    fixed = true;
    fixedServoValues[MOTOR_LU] = 1400; 
    fixedServoValues[MOTOR_RU] = 1400;
  }
  else if( strncmp("power", s, 5) == 0 ) {
    char t[4];
    for(int m=0; m <= 3; m++)
      t[m] = s[m + 5];
    t[3] = 0;
    byte p = atoi(t);
    rov.setPower(p / 100.0);
  }
}

void readSerial() {
  boolean readFlag = false;
  while(mySerial.available() > 0){
    char c = mySerial.read();
    buffer[pos++] = c;
    readFlag = true;
  }
  if(pos==64) pos = 0; //full
  
  if(readFlag == true) {
    for(int i = 0; i < pos; i++) {
      if(buffer[i] == 'a') {
        for(int j = i; j < pos; j++) {
          if(buffer[j] == '\n') {
            buffer[j] = '\0';
            processSerial(i+1, j-i); //skip a
            pos = 0;
            return;
          }
        }
      }
    }
  }
}

RTVector3 readIMU() {
    int loopCount = 1;
    RTVector3 pose;
    
    while (imu->IMURead()) {
        if (++loopCount >= 20) continue;
        fusion.newIMUData(imu->getGyro(), imu->getAccel(), imu->getCompass(), imu->getTimestamp());
        pose = fusion.getFusionPose();
        rov.reportIMU(pose.x() * RTMATH_RAD_TO_DEGREE, pose.y() * RTMATH_RAD_TO_DEGREE, pose.z() * RTMATH_RAD_TO_DEGREE);
    }
    
    return pose;
}

void controlMotors() {
  for(int i=0; i<4; i++) {
    int v = 0;
    if(fixed) v = fixedServoValues[i];
    else v = rov.servoValues[i];
    motors[i].writeMicroseconds(v);
#if 0
      Serial.print("T");
      Serial.print(i);
      Serial.print(":");
      Serial.print(v);
      Serial.print('\t');
#endif
  }
  //Serial.print('\n');
}

void loop()
{  
  //receive command
  readSerial();
  
  //read IMU, set sensor
  RTVector3 pose = readIMU();
  
  //PID control
  //output motors
  rov.step(); 
  controlMotors();
  
  //report gyro
  sendGyroData(pose);
}
