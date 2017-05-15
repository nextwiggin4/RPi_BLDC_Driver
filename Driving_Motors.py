#!/usr/bin/python

from Motor_Driver import Motor
from time import sleep

motor1 = Motor(4,17,18,0,1,2)
motor2 = Motor(5,6,12,8,9,10)
motor3 = Motor(27,22,23,4,5,6)


motor1.motorSpeed(50)
motor2.motorSpeed(50)
motor3.motorSpeed(50)

i=0

motor1.motorStep()
motor2.motorStep()
motor3.motorStep()

sleep(3)

#there are 500 steps per revolution at 100 speed.
#The number of steps per revolution is an invers relations ship
#(ie 1000 steps at 500 speed)

while (i < 368):
  motor1.motorStep()
  motor2.motorStep()
  motor3.motorStep()
  i = i + 1




