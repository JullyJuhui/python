import smtplib
from account import*
from email.message import EmailMessage

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    msg = EmailMessage()
    msg['Subject'] = '행운의 편지'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'lgy020222@gmail.com'
    

    # subject = 'message ge rong'
    # body = 'mearong leegayeon'
    # msg = f'Subject: {subject}\n{body}'
    # smtp.sendmail(EMAIL_ADDRESS, 'lgy020222@gmail.com', msg)