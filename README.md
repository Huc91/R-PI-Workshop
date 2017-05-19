# R-PI-Workshop
**WORKSHOP MATERIALS**

In this repository you can find all material needed for the workshop  

MAIN STEPS (Only Mac OS X)

SSH into the Pi --> ssh pi@<raspberry-ip>  
	*usr   pi  
	pwd   raspberry*
  
  No internet? So how to find our Pi?  
  Wire it up to the ethernet of the pc.  
    Easiest solution --> download https://github.com/adafruit/Adafruit-Pi-Finder/releases/tag/3.0.0  
      *Move Adafruit Pi Finder to Application folder.
      Find the Pi.  
      Copy the address* 
    Advanced solution --> download e use nmap  


Create a new directory called py_app   
  `sudo mkdir py_app`

Move to py_app  
  `cd py_app`

Write your script. Use what you want. I use Atom  
  https://atom.io/
    gpiozero docs --> https://gpiozero.readthedocs.io/en/stable/  
    simple example --> https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/  

Back to the terminal on the Pi  

Let's make a file to hold the script  
  `sudo touch rezine.py`

Let's edit it  
  `sudo nano rezine.py`
  Copy & Paste from Atom   
  Nano basic control:  
    *ctrl+o to save  
    ctrl+x to exit*  

**FIRE FIRE FIRE**  
  `sudo python rezine.py`

