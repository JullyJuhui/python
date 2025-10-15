#정규식
import re

pattern = re.compile('se$')  #~se
while True:
    word = input('단어> ')
    if word == '': break

    match = pattern.search(word)  #search사용**
    if match:
        print('일치')
    else:
        print('불일치')

#정규표현식: https://hamait.tistory.com/342