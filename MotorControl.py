import RPi.GPIO as GPIO
import time
import os


# Globals
class Configuration():
	Frequency = 200
	Off = 0
	Low = 20
	High = 40
	Limiter = 25
	
	M1 = None # Motor 1
	M2 = None # Motor 2
	M3 = None # Motor 3
	M4 = None # Motor 4


# Functions
def Setup(Motor1GPIO,Motor2GPIO,Motor3GPIO,Motor4GPIO):
	# Configure the GPIO Pins / Motors
	print('Configuring the GPIO Pins (Motor Pins)....')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor1GPIO,GPIO.OUT)
	GPIO.setup(Motor2GPIO,GPIO.OUT)
	GPIO.setup(Motor3GPIO,GPIO.OUT)
	GPIO.setup(Motor4GPIO,GPIO.OUT)
	GPIO.output(Motor1GPIO,False)
	GPIO.output(Motor2GPIO,False)
	GPIO.output(Motor3GPIO,False)
	GPIO.output(Motor4GPIO,False)
	Configuration.M1 = Motor1GPIO
	Configuration.M2 = Motor2GPIO
	Configuration.M3 = Motor3GPIO
	Configuration.M4 = Motor4GPIO

def Calibrate():
	# Configure the ESC's
	raw_input('Configuring the ESCs. Disconnect battery if connected and press Enter when ready.')
	Configuration.M1 = GPIO.PWM(Configuration.M1,Configuration.Frequency)
	Configuration.M2 = GPIO.PWM(Configuration.M2,Configuration.Frequency)
	Configuration.M3 = GPIO.PWM(Configuration.M3,Configuration.Frequency)
	Configuration.M4 = GPIO.PWM(Configuration.M4,Configuration.Frequency)
	Configuration.M1.start(Configuration.High)
	Configuration.M2.start(Configuration.High)
	Configuration.M3.start(Configuration.High)
	Configuration.M4.start(Configuration.High)
	raw_input('Connect Battery, Then Press Enter To Set Throttle To Low.  You will here two beeps, then wait for a gradual falling tone then press Enter')
	Configuration.M1.ChangeDutyCycle(Configuration.Low)
	Configuration.M2.ChangeDutyCycle(Configuration.Low)
	Configuration.M3.ChangeDutyCycle(Configuration.Low)
	Configuration.M4.ChangeDutyCycle(Configuration.Low)
	time.sleep(7)
	time.sleep (5)
	Configuration.M1.ChangeDutyCycle(Configuration.Off)
	Configuration.M2.ChangeDutyCycle(Configuration.Off)
	Configuration.M3.ChangeDutyCycle(Configuration.Off)
	Configuration.M4.ChangeDutyCycle(Configuration.Off)
	time.sleep(2)
	Configuration.M1.ChangeDutyCycle(Configuration.Low)
	Configuration.M2.ChangeDutyCycle(Configuration.Low)
	Configuration.M3.ChangeDutyCycle(Configuration.Low)
	Configuration.M4.ChangeDutyCycle(Configuration.Low)
	
def Arm():
	raw_input('Arming the ESCs. Battery should already be connected?')
	Configuration.M1 = GPIO.PWM(Configuration.M1,Configuration.Frequency)
	Configuration.M2 = GPIO.PWM(Configuration.M2,Configuration.Frequency)
	Configuration.M3 = GPIO.PWM(Configuration.M3,Configuration.Frequency)
	Configuration.M4 = GPIO.PWM(Configuration.M4,Configuration.Frequency)
	Configuration.M1.start(Configuration.Off)
	Configuration.M2.start(Configuration.Off)
	Configuration.M3.start(Configuration.Off)
	Configuration.M4.start(Configuration.Off)
	time.sleep(1)
	Configuration.M1.start(Configuration.High)
	Configuration.M2.start(Configuration.High)
	Configuration.M3.start(Configuration.High)
	Configuration.M4.start(Configuration.High)
	time.sleep(1)
	Configuration.M1.start(Configuration.Low)
	Configuration.M2.start(Configuration.Low)
	Configuration.M3.start(Configuration.Low)
	Configuration.M4.start(Configuration.Low)
	time.sleep(1)
	
	
# Motor Power % Setter Functions
def SetMotor1(PowerPercent):
	Max = Configuration.High - Configuration.Low
	Change = Configuration.Low+(Max*(PowerPercent/100.0))
	if(Change<Configuration.Limiter):
		#print('Setting Motor 1 To : '+str(Change) + '('+str(PowerPercent)+')')
		Configuration.M1.ChangeDutyCycle(Change)

def SetMotor2(PowerPercent):
	Max = Configuration.High - Configuration.Low
	Change = Configuration.Low+(Max*(PowerPercent/100.0))
	if(Change<Configuration.Limiter):
		#print('Setting Motor 2 To : '+str(Change) + '('+str(PowerPercent)+')')
		Configuration.M2.ChangeDutyCycle(Change)
	
def SetMotor3(PowerPercent):
	Max = Configuration.High - Configuration.Low
	Change = Configuration.Low+(Max*(PowerPercent/100.0))
	if(Change<Configuration.Limiter):
		#print('Setting Motor 3 To : '+str(Change) + '('+str(PowerPercent)+')')
		Configuration.M3.ChangeDutyCycle(Change)
	
def SetMotor4(PowerPercent):
	Max = Configuration.High - Configuration.Low
	Change = Configuration.Low+(Max*(PowerPercent/100.0))
	if(Change<Configuration.Limiter):
		#print('Setting Motor 4 To : '+str(Change) + '('+str(PowerPercent)+')')
		Configuration.M4.ChangeDutyCycle(Change)
	
def End():
	GPIO.cleanup()
