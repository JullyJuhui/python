import pandas as pd

df = pd.read_csv('data/score.csv', index_col='지원번호')

name = input('이름> ')

filt = df['이름'].str.contains(name)
df = df[filt]

if len(df.index)==0: 
    print('검색데이터가 없습니다.')

else:
    print(df)
