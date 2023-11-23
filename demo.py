##------------------------------------------
##--- Author: Pradeep Singh
##--- Blog: https://iotbytes.wordpress.com/programmatically-send-e-mail-from-raspberry-pi-using-python-and-gmail/
##--- Date: 21st Feb 2017
##--- Version: 1.0
##--- Python Ver: 2.7
##------------------------------------------
##--- Author: 1CM69
##--- Date: 23rd Nov 2023
##--- Version: 2.0
##--- Python Ver: 3.11.2
##--- Description: Just a few small changes of this great script to make it function in Python3 & also I removed the need to add the To_Add
##--- email address inside each of the scripts that you use this one by making it part of the settings.ini file
##------------------------------------------

#import the class definition from "email_handler.py" file
from email_handler import Class_eMail

# Send Plain Text Email 
email = Class_eMail()
MsgBody = ('This is a sample plain text email body.')
email.send_Text_Mail('Plain Text Mail Subject', MsgBody)
del email


# Send HTML Email
email = Class_eMail()
MsgBody = ('<html><h1>This is sample HTML test email body</h1></html>')
email.send_HTML_Mail('HTML Mail Subject', MsgBody)
del email

