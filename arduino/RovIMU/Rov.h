#ifndef ROV_H_
#define ROV_H_
#include <Arduino.h>
#include <Servo.h>

#define  SERIAL_PORT_SPEED  38400
#define DEBUG 1
#define DEBUG_MOTOR 1
#define EV3_COMM 1



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
    void right();
    void left();
    void stop();
    void step(); 
    float getRoll();
    float getPitch();
    float getYaw(); 
    int servoValues[4];
    float power;
    
  private:
    //void writeMicrosecondsForAll(int ms);
    void writeAll(int ms);
    float headingRequested;
    float powerRequested;
    float diveRequested;
    float pitch;
    float roll;
    float yaw;
    float pitch_bias;
    float roll_bias;
    float yaw_bias;
    float motorValues[4];
    //Servo motors[4];
    int count;
};
#endif
