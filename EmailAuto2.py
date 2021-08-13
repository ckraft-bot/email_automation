import csv
import email, smtplib, ssl
from email import message

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
sender_email = os.environ.get('Username')
print(sender_email)
Password = os.environ.get('Password')
print(Password)

#Log in to server using secure context and send email
smtp_server = "smtp.gmail.com"
port = 465
sender_email = os.environ.get('Username')
print(sender_email)
password = os.environ.get('Password')
print(password)
context = ssl.create_default_context()


with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    with open(r'Users/path/FileName.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            message = 'Hello ' + row[1] + '\n\nType your message here.' 
            server.login(sender_email, password)
            server.sendmail(sender_email, row[0], message)

