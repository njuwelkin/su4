import numpy as np
from loader import *


def loadAllCutSongci(path):
    f = open(path, "r")
    lines = f.readlines()
    cs = "".join(lines).split("$$$34567$$$")
    f.close()
    print(len(cs))
    return cs

dict_words = loadPZYDict('./output/words_pzy.txt')
word_idx = {k: i for i, k in enumerate(dict_words)}

cs = loadAllCutSongci("./res/all_songci_cut.txt")

cs_len = len(cs)
word_len = len(dict_words)

count_s = count_f = 0

mat = np.zeros((word_len, cs_len), dtype='float32')
for i, c in enumerate(cs):
    words = c.split('/')
    for w in words:
        w = w.strip()
        if w in [',', '.'] or len(w) == 0:
            continue
        if word_idx.get(w) is None:
            #print('************************', w)
            count_f += 1
        else:
            mat[word_idx[w], i] += 1
            #print(word_idx[w], i, w)
            count_s += 1

np.save("./output/w_c.npy", mat)
print(cs_len, word_len)
print(count_s, count_f)
