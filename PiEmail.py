{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "###################################################################################\n",
    "##      Author = 'Linghuan Zeng'\n",
    "##     License = \"Creative Commons Attribution-ShareAlike 3.0 Unported License\"\n",
    "##     Version = \"1.0\"\n",
    "##  Maintainer = \"Linghuan Zeng\"\n",
    "##      Status = \"Production\"\n",
    "###################################################################################\n",
    "\n",
    "\n",
    "import subprocess\n",
    "import smtplib\n",
    "from email.mime.image import MIMEImage\n",
    "from email.mime.text import MIMEText\n",
    "from email.mime.multipart import MIMEMultipart\n",
    "\n",
    "def email_pic(pic_name):\n",
    "\n",
    "    # Change to your own account information\n",
    "    # Account Information\n",
    "    to = 'ToEmail@gmail.com' # Email to send to.\n",
    "    gmail_user = 'FromEmail@gmail.com' # Email to send from. (MUST BE GMAIL)\n",
    "    gmail_password = 'FromEmailPassword' # Gmail password.\n",
    "    smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.\n",
    "\n",
    "    smtpserver.ehlo()  # Says 'hello' to the server\n",
    "    smtpserver.starttls()  # Start TLS encryption\n",
    "    smtpserver.ehlo()\n",
    "    smtpserver.login(gmail_user, gmail_password)  # Log in to server\n",
    "\n",
    "    # Picture paths\t\n",
    "    Photopath_org = '/home/pi/Desktop/PiCamera/PiCamera_Photos/' + pic_name\n",
    "    Photopath_rev = '/home/pi/Desktop/PiCamera/PiCamera_Photos/Rev_' + pic_name\n",
    "\t\n",
    "    # Creates the text, subject, 'from', and 'to' of the message.\n",
    "    msg = MIMEMultipart()\n",
    "    msg['Subject'] = 'PiCamera Security - ' + pic_name\n",
    "    msg['From'] = gmail_user\n",
    "    msg['To'] = to\n",
    "\t\n",
    "    # Attach the orignal picture\n",
    "    fp1 = open(Photopath_org, 'rb')\n",
    "    img_org = MIMEImage(fp1.read())\n",
    "    msg.attach(img_org)\n",
    "\n",
    "    # Attach the rotated picture\n",
    "    fp2 = open(Photopath_rev, 'rb')\n",
    "    img_rev = MIMEImage(fp2.read())\n",
    "    msg.attach(img_rev)\n",
    "\t\n",
    "    # Sends the message\n",
    "    smtpserver.sendmail(gmail_user, [to], msg.as_string())\n",
    "    # Closes the smtp server.\n",
    "    smtpserver.quit()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
