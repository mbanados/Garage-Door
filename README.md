# Garage-Door
Raspberry Pi based password protected Garage door mobile app 

This is a PHP script (index.php) that initiates a python script (gpiotoggle.py) to toggle three GPIO ports that are attached to a relay board. the intent is to toggle the garage door opener and two garage lights. The mobile app is password potected by a password you specify in the PHP script.

Setup a Raspberry Pi

Install Apache as follows:
      sudo apt-get install apache2 -y
    
Give Apache the ability to execute the scripts (Not the best method!):
      sudo visudu
          Add the following line of text:
                www-data ALL=(ALL) NOPASSWD: ALL
                
Drop these scripts in their associated directories (/var/www and /home/pi)

Edit the password in index.php (currently set to "cars")

connect your relay board (Sainsmart or otherwise) to GPIO 18, 27 and 22 or change what you need.

connect a magnetic switch to GPIO 4 as folows
	3.3 volts from RPI to 10K Ohm resistor
	10K home resistor to common on switch and to 1K Ohm resistor
	1K Ohm resistor to GPIO4
	Ground on RPI to positive on switch



Browse from your mobile phone to your device.
