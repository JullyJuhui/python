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
    msg.set_content('이 편지는 가산에서 시작되었고 메롱입니다.')

    smtp.send_message(msg)