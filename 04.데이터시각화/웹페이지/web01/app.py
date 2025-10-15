#서버가 처음 구동될때 돌아가는 파일: app.py
from flask import Flask, render_template, send_file
from io import BytesIO

import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv', index_col='지원번호')

import matplotlib.pyplot as plt

#[한글 설정]
plt.rc('font', family = 'Malgun Gothic')  #글꼴
plt.rc('font', size = 10)  #크기

plt.rc('axes', unicode_minus = False)  #마이너스

app = Flask(__name__, template_folder='templates')  #서버 생성

@app.route('/graph1')  #학생별 키 막대그래프
def graph1():
    name = df['이름']
    height = df['키']
    plt.figure(figsize=(10, 4))
    plt.bar(name, height, color='skyblue', ec='black')
    plt.ylim(150, 210)
    plt.xticks(name, rotation = 45, size=9, color='darkgreen')

    for idx, h in enumerate(height):
        plt.text(idx, h+1, f'{h}cm', ha='center', color='deeppink', size=8)

    #이미지 보내기
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')  #이미지 반환

@app.route('/graph2')  #학생별 평균점수
def graph2():
    df['평균'] = df.apply(lambda row: row['국어':'사회'].mean(), axis=1)
    name = df['이름']
    avg = df['평균']

    plt.figure(figsize=(10, 4))
    plt.bar(name, avg, color='skyblue', ec='black')
    plt.ylim(0, 100)
    plt.xticks(name, rotation = 45, size=9, color='darkgreen')

    for idx, a in enumerate(avg):
        plt.text(idx, a+1, f'{a:.2f}점', ha='center', color='deeppink', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph3')  #3.학교별 평균키
def graph3():
    group = df.groupby('학교')['키'].mean()
    labels = group.index
    values = group.values

    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color='skyblue', ec='black', width=0.5)
    plt.ylim(160, 200)
    plt.xticks(labels, rotation = 45, size=9, color='darkgreen')

    for idx, val in enumerate(values):
        plt.text(idx, val+1, f'{val:.2f}cm', ha='center', color='deeppink', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/graph4')  #4.학교별 평균점수
def graph4():
    df['평균'] = df.apply(lambda row: row['국어':'사회'].mean(), axis=1)
    group = df.groupby('학교')['평균'].mean()

    labels = group.index
    values = group.values

    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color='skyblue', ec='black', width=0.5)
    plt.ylim(0, 100)
    plt.xticks(labels, rotation = 45, size=9, color='darkgreen')

    for idx, val in enumerate(values):
        plt.text(idx, val+1, f'{val:.2f}점', ha='center', color='deeppink', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/graph5')  #5.SW특기별 인원수
def graph5():
    df['SW특기'] = df['SW특기'].str.capitalize()
    group = df.groupby('SW특기').size()
    labels = group.index
    values = group.values

    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color='skyblue', ec='black', width=0.5)
    plt.ylim(0, 6)
    plt.xticks(labels, rotation = 45, size=9, color='darkgreen')

    for idx, val in enumerate(values):
        plt.text(idx, val+0.05, f'{val}명', ha='center', color='deeppink', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html', title='학생관리')

if __name__ == '__main__':
    app.run(port=5000, debug=True)