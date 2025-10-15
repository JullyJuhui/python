import requests
from bs4 import BeautifulSoup
import os

#***
path = os.getcwd() + '/data/books' #data 밑에 books 폴더
if not os.path.exists(path):  #없으면
    os.makedirs(path)  #만들기

url = 'https://www.hanbit.co.kr/store/store_submain.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

div = soup.find('div', {'class':'new-books-container'})

imgs = div.find_all('img')

for idx, img in enumerate(imgs):
    #print(f'book{idx+1:02d}', img['src'])  #:02d) 10진수 2자리로 하고 비어있는곳은 0
    url = img['src']  #이미지가 있는 주소
    res_img = requests.get(url)

    file_name = path + f'/book{idx+1:02d}.jpg'
    with open(file_name, 'wb') as file:
        file.write(res_img.content)