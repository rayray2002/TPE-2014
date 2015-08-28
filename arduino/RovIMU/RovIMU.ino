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

//  SERIAL_PORT_SPEED defines the speed to use for the debug serial port


unsigned long lastDisplay;
unsigned long lastRate;
int sampleCount;

void initIMU() 
{
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

  lastDisplay = lastRate = millis();
  sampleCount = 0;

  fusion.setSlerpPower(0.1); //0 means that only gyros are used, 1 means that only accels/compass are used
  fusion.setGyroEnable(true);
  fusion.setAccelEnable(true);
  fusion.setCompassEnable(true);
}

void setup() 
{ 
    Serial.begin(SERIAL_PORT_SPEED);  
    initIMU();
    rov = Rov();
    rov.init();
}

void sendGyroData(RTVector3 p ) {
    if(EV3_COMM) {
              Serial.write( 'a' );
              //RTVector3 p = fusion.getFusionPose();
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
              /*
              Serial.print( p.x() * RTMATH_RAD_TO_DEGREE *  );
              Serial.print("\t");
              Serial.print( p.y() * RTMATH_RAD_TO_DEGREE );
              Serial.print("\t");
              Serial.print( p.z() * RTMATH_RAD_TO_DEGREE );
              Serial.print("\t");
              */
              //Serial.write( "\n" );
    }
}

void loop()
{  
  //receive command
  //read IMU, set sensor
  //PID control
  //output motors
  //report gyro
  
    unsigned long now = millis();
    unsigned long delta;
    int loopCount = 1;
    
    rov.setHeading(90.0f);
    rov.forward(0.12f);
    rov.up(0.12f);
    
  
    while (imu->IMURead()) {                                // get the latest data if ready yet
        // this flushes remaining data in case we are falling behind
        if (++loopCount >= 10) continue;
        fusion.newIMUData(imu->getGyro(), imu->getAccel(), imu->getCompass(), imu->getTimestamp());
        RTVector3 pose = fusion.getFusionPose();
        
        // pitch, roll, yaw, z ->pitch, y->roll, x->yaw,
        rov.reportIMU(pose.x() * RTMATH_RAD_TO_DEGREE, pose.y() * RTMATH_RAD_TO_DEGREE, pose.z() * RTMATH_RAD_TO_DEGREE);
        rov.step();
        sendGyroData(pose);
        delay(100);
       
    }
}

/*
        if ((now - lastDisplay) >= DISPLAY_INTERVAL) {
            lastDisplay = now;
            if(DEBUG) {
              //RTMath::display("Gyro:", (RTVector3&)imu->getGyro());                // gyro data
              //RTMath::display("Accel:", (RTVector3&)imu->getAccel());              // accel data
              RTMath::display("Mag:", (RTVector3&)imu->getCompass());              // compass data
              RTMath::displayRollPitchYaw("Pose:", (RTVector3&)fusion.getFusionPose()); // fused output
              
              Serial.print("\t");
              //RTVector3* mVec = (RTVector3&)imu->getCompass();
              Serial.print(((RTVector3&)imu->getCompass()).length());
              Serial.print("\t");
              Serial.println();
            }
        }
*/
