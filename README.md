# RaspberryPi_Security_Camera

Python codes to set up a Raspberry Pi security camera with Gmail notification.

The idea of this project is from Christian Cawley's article (http://www.makeuseof.com/tag/raspberry-pi-camera-module/). The capture image code in "PiCamera.py" is adapted from python codes in Christian Cawley's article.

Instructions:

1. Enable the Respberry Pi Camera:
   At the command line, enter "sudo raspi-config". In the menu select "Enable Camera", then select "Enable". Once done, select "Finish" and "Yes" to reboot.
   
2. Install the Python support for the camera:
   At the command line, enter "sudo apt-get install python-picamera python3-picamera". Once done, enter "sudo reboot".
 
3. Update the python codes: 
   Change sender's Gmail address & password and receiver's email address in "PiEmail.py". You can also customize the frequency of capturing the picture in "PiCamera.py". Please noted that, don't set to high frequency, such as "FREQ = 1"; otherwise, Google will block your gmail account. Default frequency is 60 minutes. 
 
4. Prepare python codes:
   Create a folder named "PiCamera" on your Respberry Pi desktop, and copy the "Image_Rotate.py", "PiEmail.py" and "PiCamera.py" into the "PiCamera" folder.

5. Startup script:
   At the command line, enter "sudo crontab -e". Scroll down to the very bottom and add an entry starting with @reboot: "@reboot sudo python /home/pi/Desktop/PiCamera/Image_Rotate.py & sudo python /home/pi/Desktop/PiCamera/PiEmail.py & sudo python /home/pi/Desktop/PiCamera/PiCamera.py". Once done, save and exit: press keys "Ctrl"+"X" -> "Y" -> "Enter" in order. When restart the pi, the command will be run.
   

 
References:

http://www.makeuseof.com/tag/raspberry-pi-camera-module/

http://elinux.org/RPi_Email_IP_On_Boot_Debian

https://docs.python.org/2/library/email-examples.html

http://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up
    
https://www.dexterindustries.com/howto/auto-run-python-programs-on-the-raspberry-pi/
