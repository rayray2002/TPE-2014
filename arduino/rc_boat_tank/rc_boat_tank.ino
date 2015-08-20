//5/25 mpu 9150 Serial fix




#include <SoftwareSerial.h>
#include <MsTimer2.h>
#include <Servo.h>

#define LED_L 13
#define LED_R 12

Servo r_motor;
Servo l_motor;

SoftwareSerial mySerial(10, 11);

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

int level = 20;
int l_level = 20;
int r_level = 20;
int Start;
int value = 10;
Motor motorL, motorR;

void timerIsr();

void setup() 
{
  Serial.begin(9600);
  mySerial.begin(9600);
  //mySerial.begin(9600);
  stop();
  initMotor();
  initISR();
  Serial.println("ready...");
  //mySerial.println("ready...");
}

void initMotor() {
  pinMode(LED_L, OUTPUT);
  pinMode(LED_R, OUTPUT);  
  r_motor.attach(5);
  l_motor.attach(6);

}
void initISR() {
  MsTimer2::set(10, timerIsr); // 10ms period
  MsTimer2::start();
}

int count = 0;
void loop()
{
  motorL.duty_cycle = 90;
  motorR.duty_cycle = 90;
  if (mySerial.available()) {
    count = 0;
    int raw = mySerial.read();
    //Serial.println(raw);
    if(raw != value) {
      value = raw;
      if(value == '1') 
      {
        R_forward();
      }
      else if(value == '2') 
      {
        R_backward();
      }
      else if(value == '3') 
      {
        L_forward();
      }
      else if(value == '4')
      {
        L_backward();
      }
      else if(value == '0')
      {
        stop();
      }
    }
  }
  else {
    count++;
    if(count == 800) {
      value = 100;
      //stop();
    }  
  }
} //end of loop

void R_forward()
{
  Serial.println("R_forward");
  motorR.timestamp = millis();
  motorR.cmd = CMD_Forward;
  motorR.state = Forward_On;
}

void R_backward()
{
  Serial.println("R_backward");
  motorR.timestamp = millis();
  motorR.cmd = CMD_Backward;
  motorR.state = Backward_On;
}

void L_forward()
{
  Serial.println("L_forward");
  motorL.timestamp = millis();
  motorL.cmd = CMD_Forward;
  motorL.state = Forward_On;
}

void L_backward()
{
  Serial.println("L_backward");
  motorL.timestamp = millis();
  motorL.cmd = CMD_Backward;
  motorL.state = Backward_On;
}
void stop()
{
  Serial.println("stop");
  r_motor.writeMicroseconds(1500);
  l_motor.writeMicroseconds(1500);
  motorL.cmd = CMD_Stop;
  motorL.state = Stop;
  motorR.cmd = CMD_Stop;
  motorR.state = Stop;
}
void checkMotor(Motor* motor);

void timerIsr(){
  checkMotorL();
  checkMotorR();
}

void changeValue(int* value) {
  *value = 20;
}
void checkMotorL() { 
    if(motorL.cmd == CMD_Forward) {
      if(motorL.state == Forward_On && motorL.duty_cycle < 100) {
        if( (millis() - motorL.timestamp) > motorL.duty_cycle*10) {
          digitalWrite( 13, LOW);
          l_motor.writeMicroseconds(1500);
          motorL.timestamp = millis();
          motorL.state = Forward_Off;
        }
      }
      
      if(motorL.state == Forward_Off && motorL.duty_cycle > 0) {
        if( (millis() - motorL.timestamp) > (100-motorL.duty_cycle)*10) {
          digitalWrite( 13, HIGH);
          l_motor.writeMicroseconds(1540);
          motorL.timestamp = millis();
          motorL.state = Forward_On;
        }
      }
    }
    
    if(motorL.cmd == CMD_Backward) {
      if(motorL.state == Backward_On && motorL.duty_cycle < 100) {
        if( (millis() - motorL.timestamp) > motorL.duty_cycle*10) {
          digitalWrite( 13, LOW);
          l_motor.writeMicroseconds(1500);
          motorL.timestamp = millis();
          motorL.state = Backward_Off;
        }
      }
      
      if(motorL.state == Backward_Off && motorL.duty_cycle > 0) {
        if( (millis() - motorL.timestamp) > (100-motorL.duty_cycle)*10) {
          digitalWrite( 13, HIGH);
          l_motor.writeMicroseconds(1200);
          motorL.timestamp = millis();
          motorL.state = Backward_On;
        }
      }
    }
    if(motorL.cmd == CMD_Stop) {
      digitalWrite( 13, LOW);
      l_motor.writeMicroseconds(1500);
    }
}

void checkMotorR() { 
    if(motorR.cmd == CMD_Forward) {
      if(motorR.state == Forward_On && motorR.duty_cycle < 100) {
        if( (millis() - motorR.timestamp) > motorR.duty_cycle*10) {
          digitalWrite( 12, LOW);
          r_motor.writeMicroseconds(1500);
          motorR.timestamp = millis();
          motorR.state = Forward_Off;
        }
      }
      
      if(motorR.state == Forward_Off && motorR.duty_cycle > 0) {
        if( (millis() - motorR.timestamp) > (100-motorR.duty_cycle)*10) {
          digitalWrite( 12, HIGH);
          r_motor.writeMicroseconds(1540);
          motorR.timestamp = millis();
          motorR.state = Forward_On;
        }
      }
    }
    
    if(motorR.cmd == CMD_Backward) {
      if(motorR.state == Backward_On && motorR.duty_cycle < 100) {
        if( (millis() - motorR.timestamp) > motorR.duty_cycle*10) {
          digitalWrite( 12, LOW);
          r_motor.writeMicroseconds(1500);
          motorR.timestamp = millis();
          motorR.state = Backward_Off;
        }
      }
      
      if(motorR.state == Backward_Off && motorR.duty_cycle > 0) {
        if( (millis() - motorR.timestamp) > (100-motorR.duty_cycle)*10) {
          digitalWrite( 12, HIGH);
          r_motor.writeMicroseconds(1200);
          motorR.timestamp = millis();
          motorR.state = Backward_On;
        }
      }
    }
    if(motorR.cmd == CMD_Stop) {
      digitalWrite( 12, LOW);
      r_motor.writeMicroseconds(1500);
    }
}
