from loader import *

yun_dict = loadYunDict("./output/char_yun.txt")
pz_dict = loadPZDict("output/char_pz_new.txt")
word_freq = loadFreqFile("output/words_freq.txt")

for word in word_freq.keys():
    pz_s = ""
    for c in word:
        if pz_dict.get(c) is None:
            pz = '?'
        else:
            pz = pz_dict[c]
        pz_s += pz
    if yun_dict.get(c) is None:
        yun = [100]
    else:
        yun = yun_dict[c]
    yun = " ".join(yun)
    print(word, pz_s, yun)
