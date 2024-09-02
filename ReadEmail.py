import datetime

today = datetime.date.today().strftime("%Y-%m-%d")  
print(today)
type(today)

import imaplib  # to read lib
import email  
from email.header import decode_header  
import datetime  
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
  
# creds
username = os.environ.get('gmail_user')
password = os.environ.get('gmail_key') 

import imaplib  
  
# establish a connection  
mail = imaplib.IMAP4_SSL('imap.gmail.com')  
mail.login(username, password)  
mail.select('inbox')  
  
# search for unread emails  
status, response = mail.search(None, 'UNSEEN')  
unread_emails = response[0].split()  
  
# count the number of unread emails  
num_unread_emails = len(unread_emails)  
  
print(f"You have {num_unread_emails} unread emails.")  
