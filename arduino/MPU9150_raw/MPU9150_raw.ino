#include <Servo.h>
#include "Wire.h"
#include "I2Cdev.h"
#include "MPU9150.h"
#include "helper_3dmath.h"

MPU9150 accelGyroMag;

int16_t ax, ay, az;
int16_t gx, gy, gz;
int16_t mx, my, mz;

#define LED_PIN 13
bool blinkState = false;
Servo r_motor;
Servo l_motor;

float degree;
int target = 100;
float err;
float Kp = 0.5;
float power = 1535;
float l_speed;
float r_speed;
float gain;
int i;
float value;

void setup() {
    Wire.begin();
    Serial.begin(9600);

    // initialize device
    Serial.println("Initializing I2C devices...");
    accelGyroMag.initialize();

    // verify connection
    Serial.println("Testing device connections...");
    Serial.println(accelGyroMag.testConnection() ? "MPU9150 connection successful" : "MPU9150 connection failed");

    // configure Arduino LED for
    pinMode(LED_PIN, OUTPUT);
    r_motor.attach(5);
    l_motor.attach(6);
}

void loop() {
    // read raw accel/gyro/mag measurements from device
    accelGyroMag.getMotion9(&ax, &ay, &az, &gx, &gy, &gz, &mx, &my, &mz);
    
    Serial.print(int(mx)*int(mx)); Serial.print("\t");
    Serial.print(int(my)*int(my)); Serial.print("\t");
    Serial.print(int(mz)*int(mz)); Serial.print("\t | ");

    const float N = 256;
    float mag = mx*mx/N + my*my/N + mz*mz/N;
    
    value = mag * 0.01 + value * 0.99;

    Serial.print(mag); Serial.print("\t");
    
    degree = value;
    err = target - degree;
    gain = err * Kp;
    l_speed = power + gain;
    r_speed = power - gain;
    Serial.print(l_speed);
    Serial.print(" ");
    Serial.print(r_speed);
    Serial.println();
    r_motor.write(r_speed);
    l_motor.write(l_speed);
}
