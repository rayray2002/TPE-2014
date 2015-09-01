#include <math.h>
#include "Rov.h"

float fmap(float val, float minVal, float maxVal, float low, float high) {
  return (val - minVal) * (high - low) / (maxVal - minVal) + low; 
}

Rov::Rov(){ 
}

void Rov::init() {
  motors[0].attach(3);
  motors[1].attach(5);
  motors[2].attach(6);
  motors[3].attach(9); 
  
  for(int i=0; i<NO_SERVO; i++ )
	  motorValues[i] = 0.0;

#if 1
  Serial.println("ESC calibrate start");
  writeMicroseconds(1000);
  delay(1000);
  Serial.println("ESC calibrate #2");
  writeMicroseconds(2000);
  delay(1000);
  Serial.println("ESC calibrate #3");
  writeMicroseconds(1000);
  delay(1000);
  Serial.println("ESC calibrate #4");
  writeMicroseconds(1500);
  delay(2500); //hear 3 beeps to enter RC neturel mode 
  Serial.println("ESC calibrate end");
#endif
}


void Rov::writeMicroseconds(int s) {
  motors[0].writeMicroseconds(s);
  motors[1].writeMicroseconds(s);
  motors[2].writeMicroseconds(s);
  motors[3].writeMicroseconds(s);
}

void Rov::reportIMU(float pitch_s, float roll_s, float yaw_s)
{
  pitch = pitch_s;
  roll = roll_s;
  yaw = yaw_s;
}
void Rov::setHeading(float headReq){
  headingRequested = headReq;
} 
void Rov::setDepth(float depth){
  
} 
void Rov::forward(float power){
  powerRequested = power;
}
void Rov::backward(float power){
  powerRequested = power;
} 
void Rov::up(float power){
  diveRequested = power;
} 
void Rov::down(float power){
  diveRequested = power;
}

void Rov::stop(){
  powerRequested = 0.0f;
}

void Rov::step(){
  //pitch
  float pitchDiff = pitch - 0;
  pitchDiff /= 360.0;
 
  //pitch
  float rollDiff = pitch - 0;
  rollDiff /= 360.0;
  
  //yaw
  float yawDiff = headingRequested - yaw;
  if(yawDiff>180) 
    yawDiff -= 360;
  else if (yawDiff < -180)
    yawDiff += 360;
  yawDiff /= 360.0;

#if DEBUG
  Serial.print("pow:"); Serial.print(powerRequested); Serial.print("\t");
  Serial.print("head_req:"); Serial.print(headingRequested); Serial.print("\t");
  Serial.print("pitch:"); Serial.print(pitch); Serial.print("\t");
  Serial.print("pitchDiff:"); Serial.print(pitchDiff); Serial.print("\t");
  Serial.print("roll:"); Serial.print(roll); Serial.print("\t");
  Serial.print("rollDiff:"); Serial.print(rollDiff); Serial.print("\t");
  Serial.print("yaw:"); Serial.print(yaw); Serial.print("\t");
  Serial.print("yawDiff:"); Serial.print(yawDiff); Serial.print("\t");
  Serial.println();
  //}
#endif

  powerRequested = 0; //for test
  motorValues[MOTOR_L] = powerRequested + yawDiff * YAW_KP;
  motorValues[MOTOR_R] = powerRequested + yawDiff * YAW_KP * -1;
  motorValues[MOTOR_L]  =  motorValues[MOTOR_R]  = 0;
  
  
  //deal with pitch and roll
  diveRequested = 0; //for test
  pitchDiff = 0;//for test
  //rollDiff = 0;
  motorValues[MOTOR_LU] = diveRequested + pitchDiff * PITCH_KP + rollDiff * ROLL_KP;
  motorValues[MOTOR_RU] = diveRequested + pitchDiff * PITCH_KP + rollDiff * ROLL_KP * -1;
  
  //TODO: handle reverse
  
  for(int i=0; i<NO_SERVO; i++ ) {
    int val = fmap(motorValues[i], -1.0, 1.0, 1200, 1800);
    if(val > 1700) val = 1700;
    if(val < 1300) val = 1300;
    motors[i].write(val);
    if(DEBUG_MOTOR)  Serial.print("M");
    if(DEBUG_MOTOR)  Serial.print(i);
    if(DEBUG_MOTOR)  Serial.print(":");
    if(DEBUG_MOTOR)  Serial.print(val);
    if(DEBUG_MOTOR) Serial.print('\t');
  } 
  if(DEBUG_MOTOR) Serial.println(); 
}


