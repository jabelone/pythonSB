# pythonSB
pythonSB (python Servo Blaster) is a python implementation of the Servo Blaster program.  It's main purpose is to make it easier to control servos attached to your raspberry pi directly from python.  It takes care of writing to the servo blaster file and allows you to set servo positions with a single function in python.

## License
pythonSB is released under the GNU GPL v3 or later license for all to freeky enjoy.

## Installation
This python module requires you to have the Servo Blaster program installed and running.
To to do so please follow these instructions:
1) Grab the Servo Blaster github repo from here: https://goo.gl/ERQcQh
```sudo apt-get install git```
```git clone https://github.com/richardghirst/PiBits.git```
2) Navigate to the program folder:
```cd PiBits/ServoBlaster/user```
3) Now we need to install Servo Blaster:
```sudo make install```
Depending on what dev tools you already installed you might need some others.  Open an issue on github if you need help.

Now that it is installed, servo blaster should be running.  For reference, you can use the following:
```sudo service servoblaster status``` to see the current status of servo blaster
```sudo service servoblaster start``` to start servo blaster
```sudo service servoblaster stop``` to stop servo blaster
You shouldn't have to manually start/stop it, it should start on boot automatically.

## Usage
pythonSB is very easy to use.  With just one small function you can control a servo on any GPIO pin that Servo Blaster supports.  You can see an example of how to use it in the ```example.py``` file in this repo.

1) Import the pythonSB module by doing this:
```from pythonSB import *```
2) Call the servo_set function like so:
```servo_set(12, "1500us")```
3) The example.py file has examples of different ways and explains how to use them.

## FAQ
#### The servos aren't responding to any commands
If they are "slack" or have no resistance, have they got power?  Please do NOT power them from the 5v rail on the pi.  I know it's tempting and it may work for 1 or 2 servos but it is NOT good for the pi.  Please use a separate battery or power supply.  If you're still having problems open an issue on GitHub.

#### I get an error about importing pythonSB
You need to make sure that pythonSB.py is in the same folder as you're project.  The easiest way is to download this entire GitHub repository and run the example.py command.  

#### It's still not working!
Open an issue on GitHub and I'll try to help out.
