import os

from datetime import datetime

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def send():
    todays_date = datetime.now()
    addr = 'benthayer2365@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = addr
    msg['To'] = addr
    msg['Date'] = formatdate(localtime=True)

    msg['Subject'] = 'Your world backup is ready.'

    msg.attach(MIMEText('The world backup for mc.benthayer.com is being created now as'
                        ' ~/minecraft/backups/latest.tar.gz. Today\'s date is {}'.format(
                         todays_date.strftime('%Y-%m-%d'))))

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(addr, os.getenv('EMAIL_PASSWORD'))
    s.sendmail(addr, [addr], msg.as_string())
    print('Sent email')
    s.close()


if __name__ == '__main__':
    send()
