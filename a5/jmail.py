#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jmail.py
#  

# Import smtplib for the actual sending function
import smtplib
import os
 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
 
gmail_user = "xxxx"
gmail_pwd = "xxxx"

def send(email):
	msg = MIMEMultipart()
	
	msg['From'] = gmail_user
	msg['To'] = email
	msg['Subject'] = "CSC344 Assignments"
 
	msg.attach(MIMEText("Attached are my CSC344 Assignments"))
 
	attach = "CSC344-JoeFitzsimmons.zip"
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
	msg.attach(part)
 
	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, email, msg.as_string())
	mailServer.close()
	print("Email sent to " + email) 
	
