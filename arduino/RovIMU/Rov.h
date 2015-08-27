#ifndef ROV_H_
#define CAR_H_
#include <Arduino.h>

#define MOTOR_L 0
#define MOTOR_R 1
#define MOTOR_LU 2
#define MOTOR_RU 3

class Rov{
  public:
    Rov();
    void init();
    void setHeading(int heading); // 0~360
    void setDepth(int depth); //0 ~ 200M
    void forward(int power);
    void backward(int power);
	void up(int power);
    void down(int power);
    void stop(); 
    
  private:
    int headingRequested;
    int heading;
    int powerRequested;
    float motor[4];
    
};
#endif
