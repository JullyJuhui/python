import requests

url = 'https://ad-creative.pstatic.net/image-plus/202508/htnlsfju.webp?transform=-436.0013497453803,-180.00089983025356,2100.0026994907607,1400.001799660507,684,456&bg=225,225,250&check=yes'
res = requests.get(url)

file_name = 'data/naver.jpg'
#text가 아닌건 binary data로 저장해야함
with open(file_name, 'wb') as file:
    file.write(res.content)