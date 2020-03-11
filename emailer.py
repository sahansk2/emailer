import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate


def send(subject, content, to=None, html=False, images=[]):
    addr = 'benthayer2365@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = addr
    if to is None:
        to = addr
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)

    msg['Subject'] = subject
    
    if html:
        with open(content) as content_file:
            msg.attach(MIMEText(content_file.read(), 'html'))
    else:
        msg.attach(MIMEText(content))

    for image_path in images:
        with open(image_path, 'rb') as image:
            mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-ID', '<' + image_path + '>')
        msg.attach(mime_image)

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(addr, os.getenv('EMAIL_PASSWORD'))
    s.sendmail(addr, [to], msg.as_string())
    print('Sent email')
    s.close()
