#'선형회귀 모델' 생성 함수
def model_linear():
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    dataset = pd.read_csv('data/LinearRegressionData.csv') #학습 데이터
    X = dataset.iloc[:, :-1].values  #독립변수
    y = dataset.iloc[:, -1].values  #종속변수

    reg = LinearRegression()
    reg.fit(X, y)  

    return reg

model = model_linear()

#예측점수 출력 함수
def predict(hour):
    pred = model.predict([[hour]])
    print(f'{hour}시간 공부했을때 예상점수: {pred[0]:.2f}점')

while True:
    hour = input('공부시간> ')

    if hour == '':
        break

    elif not hour.isnumeric():
        print('숫자로 입력하세요!')

    else:
        predict(int(hour))