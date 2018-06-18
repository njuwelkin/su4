from loader import *

Yun = [
    ['a', 'ia', 'ua', 'er'],
    ['o', 'uo'],
    ['e'],
    ['v', 'ii'],
    ['u'],
    ['ai', 'uai'],
    ['ei', 'ui'],
    ['ao', 'iao'],
    ['ou', 'iu'],
    ['ie', 'ue', 've'],
    ['an', 'uan'],
    ['ian', 'van'],
    ['en', 'eng'],
    ['in', 'ing', 'vn'],
    ['un'],
    ['ang', 'iang', 'uang'],
    ['ong', 'iong'],
    ['i']
]


pinyin_dict = loadPinyinDict("./res/pinyin.txt")

def getYunPart(s):
    if len(s) == 1:
        return s
    if s[:2] in ['zh', 'ch', 'sh']:
        return s[2:]
    elif s[0] in ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'r', 'z', 'c', 's', 'y', 'w']:
        yun = s[1:]
        if s[0] in ['j', 'q', 'x', 'y'] and yun[0] == 'u':
            yun = yun.replace('u', 'v')

        if s[0] in ['y']:
            if yun == 'e':
                yun = 'ie'
            elif yun == 'an':
                yun = 'ian'

        if s[0] not in ['z', 'c', 's', 'r'] and yun == 'i':
            yun = 'ii'

        return yun
    else:
        return s

for k, p in pinyin_dict.items():
    l = set()
    ret = set()
    for pinyin in p:
        y = getYunPart(pinyin)
        l.add(y)
    for y in l:
        for i in range(len(Yun)):
            if y in Yun[i]:
                ret.add(str(i))
    print(k, ' '.join(ret))


