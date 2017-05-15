#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import math
from gpiozero import LED, Button
from time import sleep

class Motor:

    #phase_shift = total_steps / 3

    
    def __init__(self, EN1, EN2, EN3, IN1, IN2, IN3):
        self.pwm = PWM(0x40)
        self.pwm.setPWMFreq(1000)
        self.EN1 = LED(EN1)
        self.EN2 = LED(EN2)
        self.EN3 = LED(EN3)
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.pwm_values = []
        self.current_step = 0
        self.total_steps = 7200
        self.speed = 0
        self.createPWVM()
        #self.createPWM()

        

    def motorOff(self):
        self.EN1.off()
        self.EN2.off()
        self.EN3.off()
        self.pwm.setPWM(self.IN1, 0, 0)
        self.pwm.setPWM(self.IN2, 0, 0)
        self.pwm.setPWM(self.IN3, 0, 0)

    def motorSpeed(self, speed):
        self.speed = speed


    def motorStep(self):
        self.current_step = (self.current_step + self.speed) % self.total_steps
        current_stepA = self.current_step
        current_stepB = (current_stepA + self.total_steps/3) % self.total_steps
        current_stepC = (current_stepA + self.total_steps/3*2) % self.total_steps
        self.EN1.on()
        self.EN2.on()
        self.EN3.on()
        self.pwm.setPWM(self.IN1, 0, self.pwm_values[current_stepA])
        self.pwm.setPWM(self.IN2, 0, self.pwm_values[current_stepB])
        self.pwm.setPWM(self.IN3, 0, self.pwm_values[current_stepC])

    def createPWVM(self):
        max_amplitude = 4721
        divisor = 1
        for step in range (0, self.total_steps):
            degree = step * 360.0/self.total_steps
            phaseA = math.sin(degree*math.pi/180.0) * max_amplitude / divisor
            phaseB = math.sin((degree-120)*math.pi/180.0) * max_amplitude / divisor
            phaseC = math.sin((degree+120)*math.pi/180.0) * max_amplitude / divisor

            voff = (min(phaseA, phaseB, phaseC) + max(phaseA, phaseB, phaseC))/2
            self.pwm_values.append((int((phaseA - voff)/2)) + (2047 / divisor))

    def createPWM(self):
        max_amplitude = 4095
        divisor = 1
        for step in range (0, self.total_steps):
            degree = step * 360.0/self.total_steps
            phaseA = math.sin(degree*math.pi/180.0) * max_amplitude / divisor

            self.pwm_values.append(int(phaseA) + (2047 / divisor))        
    
    #def motorTorque(self):
