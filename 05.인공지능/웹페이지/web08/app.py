from flask import Flask, render_template, request, send_file
from io import BytesIO
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='temp', static_folder='static')

@app.route('/data')
def data():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)
    df = df.head()
    table = df.to_html(classes='table table-striped table-hover')

    return table

@app.route('/img1')
def img1():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)

    df['year'] = df.index.year
    df['month'] = df.index.month

    group = df.groupby(['year', 'month'])[['Close', 'Volume']].mean()
    group.reset_index(inplace=True)

    plt.figure(figsize=(10,4))
    plt.plot(group.index, group['Close'], marker='s', color='deeppink')

    xticks = [x for x in group.index]
    plt.xticks(xticks, [f"{group.loc[idx, 'year']}-{group.loc[idx, 'month']}" for idx in xticks], rotation=45)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='img1/png')

@app.route('/img2')
def img2():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)

    df['year'] = df.index.year
    df['month'] = df.index.month

    group = df.groupby(['year', 'month'])[['Close', 'Volume']].mean()
    group.reset_index(inplace=True)

    plt.figure(figsize=(10,4))
    plt.bar(group.index, group['Volume'], color='orange')

    xticks = [x for x in group.index]
    plt.xticks(xticks, [f"{group.loc[idx, 'year']}-{group.loc[idx, 'month']}" for idx in xticks], rotation=45)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='img2/png')

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='주가예측')

if __name__=='__main__':
    app.run(port=5000, debug=True)