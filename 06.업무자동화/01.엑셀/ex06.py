import csv
# import pandas as pd

# file = pd.read_csv('data/score.csv')
file = open('data/score.csv', 'r', encoding='utf-8')
read_file = csv.reader(file)

scores = []
for score in read_file:
    scores.append(score)

from openpyxl import Workbook
wb = Workbook()
ws = wb.active

for score in scores:
    ws.append(score)

wb.save('data/score.xlsx')
wb.close()
print(scores)