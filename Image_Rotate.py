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
    "import Image\n",
    "\n",
    "def Img_Rotate(pic_name):\n",
    "\n",
    "    # Open the original picture\n",
    "    image_org = Image.open('/home/pi/Desktop/PiCamera/PiCamera_Photos/' + pic_name)\n",
    "\n",
    "    # Rotate the picture\n",
    "    image_rotate = image_org.rotate(90)\n",
    "\n",
    "    # Saved the rotated picture\n",
    "    image_rotate.save('/home/pi/Desktop/PiCamera/PiCamera_Photos/Rev_' + pic_name )"
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
