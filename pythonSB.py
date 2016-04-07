# Copyright Jaimyn Mayer 2016 (known as "jabelone" online)
# pythonSB is released under a GPL v3 or later license, see this
# page for the full license: http://www.gnu.org/licenses/gpl-3.0.en.html
# 
# This is a python implementation of the Servo Blaster program.
# It allows you to easily control servos attached to your pi.
# Please ensure the user service version is already running.
# (ie run the "servod" script from within the "user" folder)
# Servo Blaster Github and Docs: https://goo.gl/ERQcQh
# 
# It defaults to using the physical pin numbers on header 1.
# So if you use servo_set(12, "1500us") it would set the servo
# on physical pin 12 to a value of 1500us.  You can also use
# the built in servo definitions of servo blaster by calling
# it like this: servo_set(2, "1500us", "servo") Finally, to
# specify the physical pin on a header other than 1, call
# it like this: servo_set(12, "1500us", "header", 5)
 
import os #needed to run the Servo Blaster commands
servo_minPulse = [0]*41 #crude way of "initialising" the list
						 #41 as there is only 40 output pins
servo_maxPulse = [0]*41
servo_minAngle = [0]*41
servo_maxAngle = [0]*41

def servo_set(servoPin, servoOutput, servoPinType="", servoHeader=0):
	if (servoPinType == "servo"): #If we should use the servo numbers defined by Servo Blaster.
		os.system("echo " + str(servoPin) + "=" + servoOutput + " > /dev/servoblaster")
		#print("echo " + str(servoPin) + "=" + servoOutput + " > /dev/servoblaster") #For debugging
		
	elif (servoPinType == "header"): #If we should use physical pin number on a different header
		os.system("echo " + "P" + str(servoHeader) + "-" + str(servoPin) + "=" + servoOutput + " > /dev/servoblaster")
		#print("echo " + "P" + str(servoHeader) + "-" + str(servoPin) + "=" + servoOutput + " > /dev/servoblaster")
		
	else: #We use the physical pin number on header one by default
		os.system("echo " + "P1-" + str(servoPin) + "=" + servoOutput + " > /dev/servoblaster")
		#print("echo " + "P1-" + str(servoPin) + "=" + servoOutput + " > /dev/servoblaster")

def servo_map(value, oldMin, oldMax, newMin, newMax):
    # Figure out how 'wide' each range is
    oldSpan = oldMax - oldMin
    newSpan = newMax - newMin

    # Convert the old range into a 0-1 range (float)
    valueScaled = float(value - oldMin) / float(oldSpan)

    # Convert the 0-1 range into a value in the new range.
    return newMin + (valueScaled * newSpan)

def servo_configure(servoPin, minPulse, maxPulse, minAngle, maxAngle):
	if minPulse is not None:
		servo_minPulse[servoPin] = minPulse
	elif (servo_minPulse[servoPin] == 0):
		servo_minPulse[servoPin] = 1000
	
	if maxPulse is not None:
		servo_maxPulse[servoPin] = maxPulse
	elif (servo_maxPulse[servoPin] == 0):
		servo_maxPulse[servoPin] = 2000
	
	if minAngle is not None:
		servo_minAngle[servoPin] = minAngle
	elif (servo_minAngle[servoPin] == 0):
		servo_minAngle[servoPin] = 0
	
	if maxAngle is not None:
		servo_maxAngle[servoPin] = maxAngle
	elif (servo_maxAngle[servoPin] == 0):
		servo_maxAngle[servoPin] = 100

def servo_set_angle(servoPin, servoAngle): 
	# Currently only supports physical pin numbers. If enough interest is generated I may 
	# add support for all the diffferent types like the set_servo() funciton does above.
	# You don't have to pass the min/max parameters if you like the defaults.
	us = servo_map(servoAngle, servo_minAngle[servoPin], servo_maxAngle[servoPin], servo_minPulse[servoPin], servo_maxPulse[servoPin])
	os.system("echo " + "P1-" + str(servoPin) + "=" + str(us) + " > /dev/servoblaster")
	#print us

#servo_configure(1, 900, 2100, -90, 90) #Steering - Pin number, min us output, max us output, min angle, max angle)
#servo_configure(2, 1000, 2000, 0, 100) #Motor - Pin number, min us output, max us output, min angle, max angle)
#servo_set_angle(1, 0) #Pin number and angle
#servo_set_angle(2, 75) #Pin number and angle