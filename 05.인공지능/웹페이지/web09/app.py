from flask import Flask, render_template, request
from naverapi import getNews
from model import createModel
import re

app = Flask(__name__, template_folder='temp', static_folder='static')

vector, model = createModel()

@app.route('/predict')
def predict():
    text = request.args['text']
    find_text = re.findall(r'[가-힣]+', text)
    join_text = [' '.join(find_text)]
    vector_text = vector.transform(join_text)
    pred = model.predict(vector_text)
    if pred[0]==1:
        return "긍정"
    else:
        return "부정"

@app.route('/search')
def search():
    page = int(request.args['page'])
    display=5
    start= (page-1)*display +1
    query = request.args['query']
    items, total = getNews(query, start, display)
    data = {'items':items, 'total':total}
    return data

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='감성분석')

if __name__=='__main__':
    app.run(port=5000, debug=True)