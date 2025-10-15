from flask import Blueprint, render_template, request

bp = Blueprint('logistic', __name__, url_prefix='/logistic')

def model_logistic():
    import pandas as pd
    dataset = pd.read_csv('data/LogisticRegressionData.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    from sklearn.linear_model import LogisticRegression
    logistic = LogisticRegression()
    logistic.fit(X, y)

    return logistic

@bp.route('/predict')
def predict():
    hour = float(request.args['hour'])
    model = model_logistic()

    pred = model.predict([[hour]])
    pred_proba = model.predict_proba([[hour]])

    data = {'result': int(pred[0]), 
            'fail': f'{pred_proba[0, 0]*100:.2f}%', 
            'pass': f'{pred_proba[0, 1]*100:.2f}%'
            }
    return data

@bp.route('/predict/data')
def predict_data():
    import pandas as pd
    df= pd.read_csv('data/로지스틱회귀.csv')

    logistic = model_logistic()

    X=df.loc[:, '공부시간'].values
    X2 = X.reshape(len(X), 1)

    pred = logistic.predict(X2)
    df['pass']=pred
    df['합격예상']=df['pass'].apply(lambda x:'합격' if x==1 else '불합격')

    pred_proba = logistic.predict_proba(X2)
    pass_proba = [f'{y[1]*100:.2f}%' for y in pred_proba]  #f'{pred_proba[: ,1]*100:.2f}%'
    df['예상합격률'] = pass_proba
    df.drop(columns='pass', inplace=True)

    return df.to_html(classes='table table-striped table-hover', index=False)

@bp.route('/')
def logistic():
    import pandas as pd
    df= pd.read_csv('data/로지스틱회귀.csv')
    table = df.to_html(classes='table table-striped table-hover', index=False)
    return render_template('index.html', pageName='logistic.html',
                           title='로지스틱회귀', table=table)