#include <TimerOne.h>

typedef enum {
  CMD_Forward,
  CMD_Backward,
  CMD_Stop,
} Command;

typedef enum {
  Forward_On,
  Forward_Off,
  Stop,
  Backward_Back,
  Backward_Netural,
  Backward_On,
  Backward_Off,
} MotorState;

typedef struct {
  Command cmd;
  MotorState state;
  unsigned long timestamp;
  int duty_cycle; // 0~100%
} Motor;

Motor motorL, motorR;

void setup() 
{
  // Initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards
  pinMode(13, OUTPUT);    
  Serial.begin(38400);
  
  Timer1.initialize(10000); // 100Hz, 10ms
  Timer1.attachInterrupt( timerIsr ); // attach the service routine here
  
    forward();
}
 
void loop()
{
  // Main code loop
  // TODO: Put your regular (non-ISR) logic here

}

void forward()
{
  Serial.println("forward");
  digitalWrite( 13, HIGH);
  motorL.timestamp = millis();
  motorL.cmd = CMD_Forward;
  motorL.state = Forward_On;
  motorL.duty_cycle = 50;
}
void stop()
{
}
void backward()
{
}
 
/// --------------------------
/// Custom ISR Timer Routine
/// --------------------------
void checkMotor(Motor* motor);
void timerIsr()
{
  checkMotor( &motorL );
  //checkMotor(motorR);
}
void changeValue(int* value) {
  *value = 20;
}
void checkMotor(Motor* motor) { 
    // Toggle LED
    //digitalWrite( 13, digitalRead( 13 ) ^ 1 );
    if(motor->cmd == CMD_Forward) {
      boolean flag;
     flag = (millis() - motor->timestamp) / 10 > motorL.duty_cycle;
   
      if(motor->state == Forward_On && motor->duty_cycle < 100) {
        if( (millis() - motor->timestamp) > motor->duty_cycle*10) {
          digitalWrite( 13, LOW);
          motor->timestamp = millis();
          motor->state = Forward_Off;
        }
      }
      if(motor->state == Forward_Off && motor->duty_cycle > 0) {
        if( (millis() - motor->timestamp) > (100-motor->duty_cycle)*10) {
          digitalWrite( 13, HIGH);
          motor->timestamp = millis();
          motor->state = Forward_On;
        }
      }
    }
}
