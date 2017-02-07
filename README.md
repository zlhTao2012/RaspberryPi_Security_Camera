# RaspberryPi_Security_Camera

Python codes to set up a Respberry Pi security camera with Gmail notification.

The idea of this project is from Christian Cawley's article (http://www.makeuseof.com/tag/raspberry-pi-camera-module/). The capture image code in "PiCamera.py" is adapted from python codes in Christian Cawley's article.

Instruction:

1. Enable the Respberry Pi Camera:
   At the command line, enter "sudo raspi-config". In the menu select Enable Camera, then Finish and Yes to reboot.
   
2. Install the Python support for the camera:
   At the command line, enter "sudo apt-get install python-picamera python3-picamera". Once done, enter "sudo reboot".
 
3. Update sender's Gmail address & password and receiver's email address in "PiEmail.py".  
 
4. Prepare python codes and executable script:
   Create a folder named "PiCamera" on your Respberry Pi desktop, and copy the "Image_Rotate.py", "PiEmail.py", "PiCamera.py" and "PiCamera.sh" into the "PiCamera" folder.

5. Add script executable command to the bottom of ".bashrc" that will run "PiCamera.sh" every time you log in:
   At the command line, enter "cd ~" to make sure you are in the pi folder. Then enter "sudo nano .bashrc". Scroll down to the bottom and add the line: "./Desktop/PiCamera/PiCamera.sh". Once done, save and exit: press keys "Ctrl"+"X" -> "Y" -> "Enter" in order.
 
 
Reference:

http://www.makeuseof.com/tag/raspberry-pi-camera-module/

http://elinux.org/RPi_Email_IP_On_Boot_Debian

https://docs.python.org/2/library/email-examples.html

http://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up
    
