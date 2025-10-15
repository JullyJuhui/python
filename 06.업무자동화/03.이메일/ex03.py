import smtplib
from account import*
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '행운의 편지'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'lgy020222@gmail.com'
msg.set_content('이 편지는 가산에서 시작되었고 메롱입니다. 파일을 첨부했으니 오늘 저녁에 이것을 먹지않으면 배가 아주 고플것 입니다. 다른 음식은 먹으면 서주희와 호주에 가서 무서운 코알라 보기와 제주도 해녀 게하에서 알바하기를 해게 됩니다.')

with open('카레.png', 'rb') as file:
    msg.add_attachment(file.read(), maintype='image', subtype='png', 
                       filename = file.name)
    
with open('김주영.png', 'rb') as file:
    msg.add_attachment(file.read(), maintype='image', subtype='png', 
                       filename = file.name)

#구글 - MIME Type
with open('sample.xlsx', 'rb') as file:
    msg.add_attachment(file.read(), maintype='application', subtype='octet-stream', 
                       filename = file.name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    smtp.send_message(msg)