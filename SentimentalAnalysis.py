import csv

with open('training_data.csv') as f:
    row0words = []
    row1words = []
    common = []
    f_csv =csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row[3] == '1':
            row[2].split()
            for word in row[2]:
                if word not in row1words:
                    row1words.append(word)
        else:
            row[2].split()
            for word in row[2]:
                if word not in row0words:
                    row0words.append(word)
    for word in row1words:
        if word in row0words:
            common.append(word)
            row1words.remove(word)
    for word in row0words:
        if word in common:
            row0words.remove(word)

x = input().split()
numrow1words = 0
numrow0words = 0
for word in x:
    if word in row1words:
        numrow1words += 1
    elif word in row0words:
        numrow0words += 1

if numrow1words > numrow0words:
    print('1')
else:
    print('0')
