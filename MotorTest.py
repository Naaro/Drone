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
#MC.Calibrate()
MC.Arm()

Strength = 0
M1S = 0
M2S = 0
M3S = 0
M4S = 0
MC.SetMotor1(0)
MC.SetMotor2(0)
MC.SetMotor3(-10)
MC.SetMotor4(-10)

PGain = 0.001
HighX = 16*PGain
LowX = -18*PGain
HighY = 2*PGain
LowY = -19*PGain
def IdleTest(x,y):
	if x>HighX:
		HighX = x
	if x<LowX:
		LowX = x
	if y>HighY:
		HighY = y
	if y<LowY:
		LowY = y
	print('HighX:'+str(HighX)+'  LowX:'+str(LowX)+'  HighY:'+str(HighY)+'  LowY:'+str(LowY))

	
# Proportional Test
print('Begining Proportional Test')
x=0
y=0
try:
	while True:
		x = GYRO.getx() * PGain # Get gyro input and dampen it
		y = GYRO.gety() * PGain 
		#print('X:'+str(x)+' Y:'+str(y))
		#print('M1:'+str(M1S)+'  M2:'+str(M2S)+'  M3:'+str(M3S)+'  M4:'+str(M4S))
		#print('M1:'+str(M1S)+'  M2:'+str(M2S))
		IdleTest(x,y)
		if x>HighX:
			M1S += abs(x)
			M2S -= abs(x)
			M3S += abs(x)
			M4S -= abs(x)
		elif x<LowX:
			M1S -= abs(x)
			M2S += abs(x)
			M3S -= abs(x)
			M4S += abs(x)
		if y>HighY:
			M1S += abs(y)
			M2S += abs(y)
			M3S -= abs(y)
			M4S -= abs(y)
		elif y<LowY:
			M1S -= abs(y)
			M2S -= abs(y)
			M3S += abs(y)
			M4S += abs(y)
		MC.SetMotor1(M1S)
		MC.SetMotor2(M2S)
		#MC.SetMotor3(M3S)
		#MC.SetMotor4(M4S)
		time.sleep(.01)
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

