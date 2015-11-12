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

Browse from your mobile phone to your device.
