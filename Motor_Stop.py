#!/usr/bin/python

from Motor_Driver import Motor

motor1 = Motor(4,17,18,0,1,2)
motor2 = Motor(27,22,23,4,5,6)
motor3 = Motor(5,6,12,8,9,10)

motor1.motorOff()
motor2.motorOff()
motor3.motorOff()
