import numpy as np
from loader import *
from scipy import sparse
import math

import os, sys
utils_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "/../utils"
sys.path.append(utils_path)
import sparse_matrix


def loadAllCutSongci(path):
    f = open(path, "r")
    lines = f.readlines()
    cs = "".join(lines).split("$$$34567$$$")
    f.close()
    return cs

#dict_words = loadPZYDict('./output/words_pzy.txt')
dict_words = loadFreqFile("output/words_freq.txt")
word_idx = {k: i for i, k in enumerate(dict_words)}
dict_word_itmes = list(dict_words.items())

cs = loadAllCutSongci("./res/all_songci_cut.txt")

cs_len = len(cs)
word_len = len(dict_words)


mat = np.ones((word_len, word_len), dtype='float32')
for i, c in enumerate(cs):
    c = c.replace(',', '\n').replace('.', '\n')
    lines = c.split('\n')
    for line in lines:
        line = line.strip().strip('/').replace('//', '/').replace('//', '/').replace('//', '/')
        words = line.split('/')
        #if len(words) > 1:
        for i in range(1, len(words)):
            l, r = words[i-1], words[i]
            if word_idx.get(l) is None or word_idx.get(r) is None:
                continue
            l_idx, r_idx = word_idx[l], word_idx[r]
            mat[r_idx, l_idx] += 1
            #print(l, r)


row_sum = mat.sum(axis = 1)
col_sum = mat.sum(axis = 0)

print(1)
mat = np.log(mat)
print(2)
row_sum = np.log(row_sum)
col_sum = np.log(col_sum)
print(3)

for i in range(word_len):
    mat[i] /= col_sum
mat = mat.T
print(4)
for j in range(word_len):
    mat[j] /= row_sum
mat = mat.T


print(5)
most_freq_words = [i for i, (k, v) in enumerate(dict_word_itmes) if int(v) >= 60]
sim = np.zeros((word_len, word_len), dtype='float32')

for idx_i in range(len(most_freq_words)):
    i = most_freq_words[idx_i]
    print(i)
    print(dict_word_itmes[i][0], dict_word_itmes[i][1])
    for idx_j in range(idx_i+1, len(most_freq_words)):
        j = most_freq_words[idx_j]
        if mat[i, j] == 0:
            continue
        vli, vri = mat[i], mat[:, i]
        vlj, vrj = mat[j], mat[:, j]
        delta_l = math.sqrt(sum((vli - vlj)**2))
        delta_r = math.sqrt(sum((vri - vrj)**2))
        sim[i, j] = 2.0 / (delta_l + delta_r)


coo = sparse.csr_matrix(mat + mat.T)
sparse_matrix.save_sparse_csr("./output/sim.npy", coo)
