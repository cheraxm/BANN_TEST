# #Email
import os
# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
# import pandas as pd




# Define the HTML document
# def sendCustomEmail():
#     import codecs
#     myhtmlattachment = codecs.open("emailtemplate.html", 'r')
#     html = myhtmlattachment.read()
def sendCustomEmail(email_inerhtmlData):
    html = email_inerhtmlData

    email_sender = 'nttpS031103@gmail.com'
    email_password = "aodwkxfcymsrrluu"
    email_receiver = 'sweetieton4321@gmail.com'

    subject = 'ชะเอมเป็นคนสวยแต่โทษที ข้าวสวยกว่า'
    body = """
    Cat lover Cat lover Cat lover Cat lover
    """

    message = EmailMessage()
    message = MIMEMultipart()
    message["From"] = email_sender
    message["To"] = email_receiver
    message["Subject"] = subject
    # message.set_content(body)

    message.attach(MIMEText(html, "html"))
    email_string = message.as_string()


    context = ssl.create_default_context()

    # with smtplib.SMTP_SSL(host="smtp.gmail.com", port=587) as smtp:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, email_string)
    print('SENT')
