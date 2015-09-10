#include <math.h>
#include "Rov.h"

int fmap(float val, float minVal, float maxVal, float low, float high) {
  return (int)((val - minVal) * (high - low) / (maxVal - minVal) + low); 
}

#define MOTOR_L 0
#define MOTOR_R 1
#define MOTOR_LU 2
#define MOTOR_RU 3
#define NO_SERVO 4

Rov::Rov(){ 
}

void Rov::init() {

  pitch_bias = 0.0f;
  roll_bias = 0.0f;
  yaw_bias = 0.0f;
  for(int i=0; i<NO_SERVO; i++ )
	  motorValues[i] = 0.0;
  headingRequested = 0.0f;
  powerRequested = 0.0f;
  diveRequested = 0.0f;
  power = 0.0f;
}

void Rov::reportIMU(float pitch_s, float roll_s, float yaw_s)
{
  if(pitch_bias==0 && pitch_bias==0 && pitch_bias==0) {
     pitch_bias = pitch_s;
     roll_bias = roll_s;
     yaw_bias = yaw_s;
  }
  pitch = pitch_s;
  roll = roll_s;
  yaw = yaw_s;
}
void Rov::setHeading(float headReq){
  headingRequested = headReq;
} 
float Rov::getHeading(){
  return yaw;
} 
void Rov::setDepth(float depth){
  diveRequested = depth;
} 
void Rov::setPower(float p){
  power = powerRequested = p;
} 
void Rov::forward(){
  power = powerRequested;
}
void Rov::backward(){
  power = powerRequested*-1;
} 
void Rov::up(){
  //power = powerRequested;
  diveRequested = 0.5f;
} 
void Rov::down(){
  diveRequested = -0.5f;
}
void Rov::stop(){
  power = 0.0f;
  diveRequested = 0.0f;
}
float Rov::getPitch(){
  return (pitch - pitch_bias) * -1;
}
float Rov::getRoll(){
  return (roll - roll_bias) * -1;
}
float Rov::getYaw(){
  return (yaw - yaw_bias) * -1;
}

#define PITCH_KP  8.0
#define ROLL_KP 5.0
#define YAW_KP   4.0
void Rov::step(){
  boolean display_flag =  count++ %100 ==0;
  
  //pitch
  float pitchDiff = getPitch() - 0;
  pitchDiff = pitchDiff / 360.0 * PITCH_KP;
  
  //roll
  float rollDiff = getRoll() - 0;
  rollDiff = rollDiff / 360.0 * ROLL_KP;
  
  //yaw
  float yawDiff = headingRequested - getYaw();
  if(yawDiff>180) 
    yawDiff -= 360;
  else if (yawDiff < -180)
    yawDiff += 360;
  yawDiff /= 360.0;
  yawDiff *= YAW_KP;

  if(DEBUG && display_flag) {
    Serial.print("pow:"); Serial.print(powerRequested); Serial.print("\t");
    Serial.print("head_req:"); Serial.print(headingRequested); Serial.print("\t");
    Serial.print("pitch:"); Serial.print(getPitch()); Serial.print("\t");
    Serial.print("pitchDiff:"); Serial.print(pitchDiff); Serial.print("\t");
    Serial.print("roll:"); Serial.print(getRoll()); Serial.print("\t");
    Serial.print("rollDiff:"); Serial.print(rollDiff); Serial.print("\t");
    Serial.print("yaw:"); Serial.print(getYaw()); Serial.print("\t");
    Serial.print("yawDiff:"); Serial.print(yawDiff); Serial.print("\t");
    Serial.println();
  }

  //powerRequested = 0; //for test
  motorValues[MOTOR_L] = power + yawDiff;
  motorValues[MOTOR_R] = power + yawDiff * -1;
  
  //deal with pitch and roll
  //diveRequested = 0; //for test
  //pitchDiff = 0;//for test
  //rollDiff = 0;
  motorValues[MOTOR_LU] = diveRequested + pitchDiff + rollDiff * -1;
  motorValues[MOTOR_RU] = diveRequested + pitchDiff + rollDiff;
  
  //TODO: handle reverse
  for(int i=0; i<NO_SERVO; i++ ) {
    int val = fmap(motorValues[i], -1.0, 1.0, 1350, 1650);
    if(val > 1650) val = 1650;
    if(val < 1350) val = 1350;
 
    if(DEBUG_MOTOR && display_flag)  {
      Serial.print("M");
      Serial.print(i);
      Serial.print(":");
      Serial.print(val);
      Serial.print('\t');
    }
    if(i==2) val = 1500 - (val - 1500); //only for LU
    if(val < 1550 && val > 1450) val = 1500;
    servoValues[i] = val;
  } 
  if(DEBUG_MOTOR && display_flag) Serial.println(); 
}


