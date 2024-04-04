# read data from file 'MBTI-data.csv'
# 'MBTI-filter.csv' is the filtered (valid) data

f = open('MBTI-data.csv', encoding='UTF-8')
fr = f.readlines()
s = ''

for line in fr:
    key = line.split('|')[1]
    if key.count(',') > 1 or key == 'N\n':
        continue
    s += line

f = open('MBTI-filter.csv', mode='w', encoding='UTF-8')
f.write(s)
f.close()