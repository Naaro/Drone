#import gyo as gyro
import RPi.GPIO as GPIO
import time
import os
import MotorControl as MC

print('Run Setup')
I = input('')
MC.Setup(38,29,35,26)
print('Configuring and starting Motors')
I = input('')
MC.Start()

Strength = 0

try:
	while Strength<30:
		os.system('clear')
		print('Strength = ' + str(Strength))
		I = input('Set Strength (100 Max) : ')
		Strength=float(I)
		MC.SetMotor1(Strength)
		MC.SetMotor2(Strength)
		MC.SetMotor3(Strength)
		MC.SetMotor4(Strength)
		time.sleep(.25)
except KeyboardInterrupt:
	MC.End()
except:
	MC.End()

