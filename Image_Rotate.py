###################################################################################
##      Author = 'Linghuan Zeng'
##     License = "Creative Commons Attribution-ShareAlike 3.0 Unported License"
##     Version = "1.0"
##  Maintainer = "Linghuan Zeng"
##      Status = "Production"
###################################################################################

import Image

def Img_Rotate(pic_name):

    # Open the original picture
    image_org = Image.open('/home/pi/Desktop/PiCamera/PiCamera_Photos/' + pic_name)

    # Rotate the picture
    image_rotate = image_org.rotate(90)

    # Saved the rotated picture
    image_rotate.save('/home/pi/Desktop/PiCamera/PiCamera_Photos/Rev_' + pic_name )


