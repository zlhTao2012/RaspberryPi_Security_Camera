###################################################################################
##      Author = 'Linghuan Zeng'
##     License = "Creative Commons Attribution-ShareAlike 3.0 Unported License"
##     Version = "1.0"
##  Maintainer = "Linghuan Zeng"
##      Status = "Production"
###################################################################################


import subprocess
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def email_pic(pic_name):

    # Change to your own account information
    # Account Information
    to = 'ToEmail@gmail.com' # Email to send to.
    gmail_user = 'FromEmail@gmail.com' # Email to send from. (MUST BE GMAIL)
    gmail_password = 'FromEmailPassword' # Gmail password.
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

    smtpserver.ehlo()  # Says 'hello' to the server
    smtpserver.starttls()  # Start TLS encryption
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_password)  # Log in to server

    # Picture paths	
    Photopath_org = '/home/pi/Desktop/PiCamera/PiCamera_Photos/' + pic_name
    Photopath_rev = '/home/pi/Desktop/PiCamera/PiCamera_Photos/Rev_' + pic_name
	
    # Creates the text, subject, 'from', and 'to' of the message.
    msg = MIMEMultipart()
    msg['Subject'] = 'PiCamera Security - ' + pic_name
    msg['From'] = gmail_user
    msg['To'] = to
	
    # Attach the orignal picture
    fp1 = open(Photopath_org, 'rb')
    img_org = MIMEImage(fp1.read())
    msg.attach(img_org)

    # Attach the rotated picture
    fp2 = open(Photopath_rev, 'rb')
    img_rev = MIMEImage(fp2.read())
    msg.attach(img_rev)
	
    # Sends the message
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    # Closes the smtp server.
    smtpserver.quit()
