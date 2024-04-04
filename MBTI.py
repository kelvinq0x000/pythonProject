# set variable NAMES as the scientist names data with '|' split
# MBTI-data.csv is the data of each scientist and their MBTI (UTF-8)
# Create by Kelvin Q

import requests as req


def calc(res, MBTI):
    count = list(map(res.count, MBTI))
    mx = 0
    mxi = [-1]
    for i in range(len(count)):
        if count[i] > mx:
            mx = count[i]
            mxi = [i]
        elif count[i] == mx and count[i] != 0:
            mxi.append(i)
    if mxi == [-1]:
        return 'N'
    return [MBTI[i] for i in mxi]

MBTI = [a+b+c+d for a in "IE"
                for b in "SN"
                for c in "TF"
                for d in "JP"]

NAMES = "Wilhelm Conrad Röntgen|Hendrik Antoon Lorentz"

s = ''

for name in NAMES.split('|'):
    url = f"https://www.google.com/search?q=MBTI+{name.replace(' ', '+')}"
    res = req.get(url)
    res = str(res.text)
    r = calc(res, MBTI)
    s += name + '|'
    s += ','.join(r) + '\n'

f = open('MBTI-data.csv', mode='w', encoding='UTF-8')
f.write(s)
f.close()
