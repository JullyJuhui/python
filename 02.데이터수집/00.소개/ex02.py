import requests

url = 'https://www.lottecinema.co.kr/NLCHS/Movie/List?flag=1'
#사람으로 인식하도록 - user agent string
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
res = requests.get(url, headers = headers)

file_name = 'data/lottecinema.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)