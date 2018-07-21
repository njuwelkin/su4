import numpy as np
from loader import *
from scipy import sparse

import os, sys
utils_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "/../utils"
sys.path.append(utils_path)
import sparse_matrix


def loadAllSongci(path):
    f = open(path, "r")
    lines = f.readlines()
    cs = "".join(lines).split("$$$34567$$$")
    f.close()
    print(len(cs))
    return cs

dict_words = loadPZYDict('./output/words_pzy.txt')
word_idx = {k: i for i, k in enumerate(dict_words)}

cs = loadAllSongci("./res/all_songci_raw.txt")

cs_len = len(cs)
word_len = len(dict_words)

mat = np.zeros((word_len, cs_len), dtype='float32')
for j, c in enumerate(cs):
    #print(c)
    for i, w in enumerate(dict_words.keys()):
        mat[i, j] = c.count(w)


#np.save("./output/w_c.npy", mat)
print(cs_len, word_len)

coo = sparse.csr_matrix(mat)
print(1)
sparse_matrix.save_sparse_csr("./output/w_c.npy", coo)

