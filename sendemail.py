import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def send(subject, text):
    addr = 'benthayer2365@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = addr
    msg['To'] = addr
    msg['Date'] = formatdate(localtime=True)

    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(addr, os.getenv('EMAIL_PASSWORD'))
    s.sendmail(addr, [addr], msg.as_string())
    print('Sent email')
    s.close()
