##------------------------------------------
##--- Author: Pradeep Singh
##--- Blog: https://iotbytes.wordpress.com/programmatically-send-e-mail-from-raspberry-pi-using-python-and-gmail/
##--- Date: 21st Feb 2017
##--- Version: 1.0
##--- Python Ver: 2.7
##------------------------------------------



#import the class definition from "email_handler.py" file
from email_handler import Class_eMail

#set the email ID where you want to send the test email 
To_Email_ID = "pradeep.si@gmail.com"


# Send Plain Text Email 
email = Class_eMail()
email.send_Text_Mail(To_Email_ID, 'Plain Text Mail Subject', 'This is sample plain test email body.')
del email


# Send HTML Email
email = Class_eMail()
email.send_HTML_Mail(To_Email_ID, 'HTML Mail Subject', '<html><h1>This is sample HTML test email body</h1></html>')
del email

