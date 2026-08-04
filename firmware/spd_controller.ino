/*
 * PROJECT SERENA - Smart Pill Dispenser (SPD)
 * Microcontroller: ESP32
 * Actuation: Stepper Motor (Carousel) + Servo Motor (Gate)
 */

#include <ESP32Servo.h>

#define SERVO_PIN 18
#define STEP_PIN 19
#define DIR_PIN 21

Servo gateServo;

void setup() {
  Serial.begin(115200);
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  
  gateServo.attach(SERVO_PIN);
  gateServo.write(0); // Close gate by default
  
  Serial.println("[SPD] Smart Pill Dispenser Initialized.");
}

void rotateCarousel(int steps) {
  digitalWrite(DIR_PIN, HIGH);
  for(int x = 0; x < steps; x++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(1000);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(1000);
  }
}

void dispensePill() {
  Serial.println("[SPD] Dispensing pill...");
  gateServo.write(90); // Open gate
  delay(1000);
  gateServo.write(0);  // Close gate
}

void loop() {
  // Receives scheduled signals from Firebase / Central controller
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == 'D') { // Trigger Dispense
      rotateCarousel(200); // Rotate bin
      dispensePill();
    }
  }
}
