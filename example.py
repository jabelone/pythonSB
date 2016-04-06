# Copyright Jaimyn Mayer 2016 (known as "jabelone" online)
# pythonSB is released under a GPL v3 or later license, see this
# page for the full license: http://www.gnu.org/licenses/gpl-3.0.en.html
# This is part of pythonSB.  Github here: https://github.com/jabelone/pythonSB
# This shows to use all features of pythonSB
# 
# You can remove the commented print statements in pythonSB.py to see the exact output of the functions.
# 
# Most servos have a range from about 1000us to about 2000us.
# 1000us/2000us is normally the extremes and 1500us is centered.  

from pythonSB import * #We need to import the pythonSB module

servo_set(12, "1500us") #Set the servo attached to physical pin 12 on header 1 to 1500us.

servo_set(12, "+10us")  #Set the servo attached to physical pin 12 on header 1 to 10us higher.
						#This will step the value up (+10us) or down (-10us) It will round down to the
					    #nearest stepsize so +1us may not do even do anything anything!
						
servo_set(1, "1500us", "servo") #Set the servo attached to "servo pin" 1 to 1500us.

servo_set(12, "1500us", "header", 5) #Set the servo attached to physical pin 12 on header 5 to 1500us.
