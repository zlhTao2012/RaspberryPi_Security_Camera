###################################################################################
##      Author = 'Linghuan Zeng'
##     License = "Creative Commons Attribution-ShareAlike 3.0 Unported License"
##     Version = "1.0"
##  Maintainer = "Linghuan Zeng"
##      Status = "Production"
###################################################################################

import os
import time
import picamera
import PiEmail as PiEmail
import Image_Rotate as Image_Rotate
 
VIDEO_DAYS = 1 # How many days of picture capturing
FREQ = 60 # Frequency in minute of picture capturing in VIDEO_DAYS, must be integer
FRAMES = FREQ * 24 * VIDEO_DAYS

# Function of capture picture
def capture_frame(pic_name):

    with picamera.PiCamera() as cam:

        time.sleep(1)

        cam.capture('/home/pi/Desktop/PiCamera/PiCamera_Photos/' + pic_name)


# Capture the images
for frame in range(int(FRAMES)):

    # Note the time before the capture
    start = time.time() 

    # Timestamp of the pict capturing
    timestr = time.strftime("%Y%m%d_%H%M%S")  

    # Picture name
    pic_name = 'Photo' + timestr + '.jpg'       

    # Capture the picture
    capture_frame(pic_name)

    print 'Picture took!'

    time.sleep(1)

    # Rotate the picture
    Image_Rotate.Img_Rotate(pic_name)
    
    print 'Picture rotated!'

    time.sleep(1)

    PiEmail.email_pic(pic_name)

    print 'Pictures sent!'

    # Calculating the delay and wait for next capture

    Wait_time = int(FREQ * 60 - (time.time() - start))

    print 'Wait ' + str(Wait_time) + ' seconds for next capture!'

    time.sleep(Wait_time)
    
    # Deleted previous photos
    os.remove('/home/pi/Desktop/PiCamera/PiCamera_Photos/' + pic_name)
    os.remove('/home/pi/Desktop/PiCamera/PiCamera_Photos/Rev_' + pic_name)

    print 'Pictures deleted!'