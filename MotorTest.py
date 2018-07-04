import gyro as GYRO
import RPi.GPIO as GPIO
import time
import os
import MotorControl as MC

print('Running MC.Setup')
#raw_input('Press Enter To Continue...')
MC.Setup(38,29,35,26)

print('Running MC.Start to Configure the Motors')
#raw_input('Press Enter To Continue...')
MC.Start()


Strength = 0
MC.SetMotor1(Strength)
MC.SetMotor2(Strength)
MC.SetMotor3(Strength)
MC.SetMotor4(Strength)


# Proportional Test
print('Begining Proportional Test')
PGain = 0.0001
x=0
y=0
try:
	while True:
		x = GYRO.getx() * PGain # Get gyro input and dampen it
		y = GYRO.gety() * PGain 
		#print('X:'+str(x)+' Y:'+str(y))
		#x+=1
		#y+=1
		time.sleep(.25)
except KeyboardInterrupt:
	MC.End()
except:
	MC.End()
	
exit()
	
# Direct Motor Control Test
try:
	while Strength<30:
		os.system('clear')
		print('Strength = ' + str(Strength))
		I = input('Set % Strength (100 Max) : ')
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

