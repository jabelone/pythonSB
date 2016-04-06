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
		