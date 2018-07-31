import numpy as np
from loader import *
from scipy import sparse
import math

import os, sys
utils_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "/../utils"
sys.path.append(utils_path)
import sparse_matrix


def loadAllCutSongciLines(path):
    f = open(path, "r")
    lines = f.readlines()
    cs = "".join(lines).split("$$$34567$$$")
    f.close()
    ret = []
    for line in lines:
        line = line.strip().strip('/').replace(',', '\n').replace('.', '\n')
        ls = line.split('\n')
        for l in ls:
            if len(l) == 0 or l == '$$$34567$$$':
                continue
            ret.append(l)
    return ret

dict_words = loadPZYDict('./output/words_pzy.txt')
word_idx = {k: i for i, k in enumerate(dict_words)}
dict_word_itmes = list(dict_words.items())
print(len(dict_word_itmes))

lines = loadAllCutSongciLines("./res/all_songci_cut.txt")
print("lines: ", len(lines))

cs_len = len(lines)
word_len = len(dict_words)
mat = np.zeros((word_len, cs_len), dtype='float32')

for i, line in enumerate(lines):
    words = line.split('/')
    for w in words:
        w = w.strip()
        if w in [',', '.'] or len(w) == 0:
            continue
        if word_idx.get(w) is None:
            #print('************************', w)
            continue
        else:
            mat[word_idx[w], i] += 1

coo = sparse.csr_matrix(mat)
sparse_matrix.save_sparse_csr("./output/w_c3.npy", coo)

