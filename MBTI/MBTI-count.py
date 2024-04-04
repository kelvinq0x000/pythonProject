# read data from file 'MBTI-filter.csv'
# the program will ouput the result directly

f = open('MBTI-filter.csv', encoding='UTF-8')
r = f.read()
f.close()

MBTI = [a+b+c+d for a in "IE"
                for b in "SN"
                for c in "TF"
                for d in "JP"]
res = list(map(r.count,MBTI))
for i in range(len(res)):
    print(MBTI[i], res[i])