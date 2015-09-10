#include <Wire.h>
#include "I2Cdev.h"
#include "RTIMUSettings.h"
#include "RTIMU.h"
#include "RTFusionRTQF.h" 
#include "CalLib.h"
#include "Rov.h"
#include <EEPROM.h>

RTIMU *imu;                                           // the IMU object
RTFusionRTQF fusion;                                  // the fusion object
RTIMUSettings settings;                               // the settings object
Rov rov;

//  DISPLAY_INTERVAL sets the rate at which results are displayed
#define DISPLAY_INTERVAL  100                         // interval between pose displays
#define LIGHT_PIN 13
#define CAMERA_PIN 12

unsigned long lastDisplay;
unsigned long lastRate;
int sampleCount;

void setup() 
{
    Serial.begin(SERIAL_PORT_SPEED);
    pinMode(LIGHT_PIN, OUTPUT);
    pinMode(CAMERA_PIN, OUTPUT);
    
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
}

void sendGyroData(RTVector3 p ) {
#ifdef EV3_COMM
    Serial.write( 'a' );
    short x = p.x() * RTMATH_RAD_TO_DEGREE * 100;
    Serial.write( (byte)x );
    Serial.write( (byte)(x >> 8) );
    short y = p.y() * RTMATH_RAD_TO_DEGREE * 100;
    Serial.write( (byte)y );
    Serial.write( (byte)(y >> 8) );
    short z = p.z() * RTMATH_RAD_TO_DEGREE * 100;
    Serial.write( (byte)z );
    Serial.write( (byte)(z >> 8) );
    Serial.write( '\n' );
#endif 
}
    
char buffer[64];
int pos = 0;
void processSerial(int index, int len) {
  char s[len];
  
  for(int i=0; i< len; i++)
    s[i] = buffer[i+index];
    
  //Serial.print(">>");
  //Serial.println(s);
  
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
  }
  else if( strcmp("backward", s) == 0) {
    rov.backward();
  }
  else if( strcmp("stop", s) == 0) {
    rov.stop();
  }
  else if( strcmp("right", s) == 0) {
    rov.setHeading( rov.getHeading() + 20);
  }
  else if( strcmp("left", s) == 0) {
    rov.setHeading( rov.getHeading() + 20);
  }
  else if( strcmp("up", s) == 0) {
    rov.up();
  }
  else if( strcmp("down", s) == 0) {
    rov.down();
  }
  else if( strncmp("power", s, 5) == 0 ) {
    char t[3];
    for(int m=0; m <= 3; m++)
      t[m] = s[m + 5];
    byte p = atoi(t);
    rov.setPower(p / 100.0);
  }
}

void readSerial() {
  boolean readFlag = false;
  while(Serial.available() > 0){
    char c = Serial.read();
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
            processSerial(i+1, j-i);
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
    
    rov.setHeading(70.0f);
    //rov.forward(0.12f);
    //rov.up(0.5f);
  
    while (imu->IMURead()) {                                // get the latest data if ready yet
        // this flushes remaining data in case we are falling behind
        if (++loopCount >= 20) continue;
        fusion.newIMUData(imu->getGyro(), imu->getAccel(), imu->getCompass(), imu->getTimestamp());
        pose = fusion.getFusionPose();
        rov.reportIMU(pose.x() * RTMATH_RAD_TO_DEGREE, pose.y() * RTMATH_RAD_TO_DEGREE, pose.z() * RTMATH_RAD_TO_DEGREE);
    }
    return pose;
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
  //report gyro
  sendGyroData(pose);
}
