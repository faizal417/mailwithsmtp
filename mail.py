#!/usr/bin/python3

import smtplib
from email.encoders import encode_base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Testing Email Spoofing"

user="faizal" #username

email = "user@domain.com" #sender's email

recipient = "" # recipient's mail

smtp="127.0.0.1" # ip address of smtp server

port = int(25) #smtp port on smtp server

password="" #password of the user's email address

text_body="This is just a text mail for testing purpose."

html_body="<html><h1>This is a test mail from Python script.</h1></html>"

#Sending the email with a smtp server
def sendMail(subject, email, password, recipient, text_body, smtp, port,html_body):
        msg = MIMEMultipart('alternative')
        msg['From'] = email
        msg['To'] = recipient
        msg['Subject'] = subject 
        msg.attach(MIMEText(text_body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))
        msg.add_header('Content-Transfer-Encoding', 'base64')
        try:
                server = smtplib.SMTP(smtp, int(port))
                server.ehlo()
                server.starttls()
                server.ehlo()
                text = msg.as_string()
                server.sendmail(email, recipient.split(","), text)
                server.quit()
                print("try")
                print(text)
                return 'ok'
        except Exception as err:
                print("except")
                print(err)
                pass
                return err
sendMail(subject, email, password, recipient, text_body, smtp, port, html_body)
