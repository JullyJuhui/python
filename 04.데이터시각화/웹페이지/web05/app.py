from flask import Flask, render_template, request, send_file

app=Flask(__name__, template_folder='temp')

@app.route('/')
def health():
    return render_template('health.html')  #temp 파일의 health.html

@app.route('/health/graph')
def health_graph():
    from io import BytesIO

    import matplotlib.pyplot as plt
    plt.rc('font', family = 'Malgun Gothic')
    plt.rc('font', size=5)
    plt.rc('axes', unicode_minus=False)

    import pandas as pd
    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')

    word = request.args['word']
    filt = df['시도군구'].str.contains(word)
    df = df[filt]

    if len(df)>0:
        df = df[:10]

    plt.title('지역별 공공의료기관 수', size=20)
    plt.barh(df['시도군구'], df['count'])

    # for idx, c in enumerate(df['count']):
    #     plt.text(c+0.1, idx, c, va='center')

    # plt.show()
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype = 'image/png')

@app.route('/health/data')
def health_data():
    import pandas as pd

    page = int(request.args['page'])
    size = int(request.args['size'])
    word = request.args['word']

    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')
    filt = df['시도군구'].str.contains(word)
    df = df[filt]

    start = (page-1)*size
    end = page*size
    df2 = df[start:end]
    count =len(df)
    table = df2.to_html(index=False, classes='table table-light table-hover')  #table-striped-columns 

    data = {'count':count, 'table':table}
    return data

if __name__=='__main__':
    app.run(port=5000, debug=True)
