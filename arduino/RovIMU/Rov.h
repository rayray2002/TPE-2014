#ifndef ROV_H_
#define ROV_H_
#include <Arduino.h>
#include "Servo.h"

#define  SERIAL_PORT_SPEED  38400
#define DEBUG 1
#define DEBUG_MOTOR 1
//#define EV3_COMM

#define MOTOR_L 0
#define MOTOR_R 1
#define MOTOR_LU 2
#define MOTOR_RU 3
#define NO_SERVO 4

/*
int data[NO_SERVO][8] = {
  {3,  A1, 90,  90,  20, 160, 30, 0}, //BASE
  {5,  A0, 90,  90,  45, 160, 20, 0}, //LOW
  {6,  A5, 140, 140, 60, 160, 20, 0}, //UPPER
  {10, A4, 90,  90,  70, 110, 40, 0}, //GRIP
};
*/

class Rov{
  public:
    Rov();
    void init();
    void setHeading(float heading); // 0~360
    float getHeading(); 
    void setDepth(float depth); //0 ~ 200M
    void setPower(float power); //0 ~ 100
    void reportIMU(float pitch, float roll, float yaw);
    void forward();
    void backward();
    void up();
    void down();
    void stop();
    void step(); 
    float getRoll();
    float getPitch();
    float getYaw(); 
    
  private:
    void writeMicrosecondsForAll(int ms);
    float headingRequested;
    float powerRequested;
    float diveRequested;
    float pitch;
    float roll;
    float yaw;
    float pitch_bias;
    float roll_bias;
    float yaw_bias;
    float power;
    float motorValues[4];
    Servo motors[4];
};
#endif
