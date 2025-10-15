# 네이버 검색 API 예제 - 블로그 검색
import urllib.request
import json

def getNews(query, start, display):  #defalut:, 1, 10
    client_id = "DSISkunI4gxjpwj6Yl6J"
    client_secret = "CxLnF9_VmQ"
    encText = urllib.parse.quote(query)
    # JSON 결과
    url = f"https://openapi.naver.com/v1/search/news.json?query={encText}&start={start}&display={display}"  
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        # print(response_body.decode('utf-8'))
        return result['items'], result['total']
    
    else:
        print("Error Code:" + rescode)
        return None