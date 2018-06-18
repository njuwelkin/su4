import numpy as np
from scipy import sparse 
import utils.loader as loader

import os, sys
utils_path = os.path.dirname(os.path.abspath(__file__)) + "/../utils"
sys.path.append(utils_path)
import sparse_matrix

class Relevancy(object):
    def __init__(self):
        # ww: N * N
        self._ww = sparse_matrix.load_sparse_csr("./res/w_w.npy.npz").toarray()

        self.words = loader.loadKeyValues('./res/words_pzy.txt')
        self.word_idx = {k: i for i, (k,v) in enumerate(self.words.items())}
        self.word_itmes = list(self.words.keys())

        to_find = 3
        self.seg_start = [0, 0, 0, 0]
        self.seg_end = [0, len(self.word_itmes), 0, 0]
        for i, w in enumerate(self.word_itmes):
            if len(w) == to_find:
                if to_find == 3:
                    self.seg_start[3] = i
                    self.seg_end[2] = i
                    to_find = 1
                else:
                    self.seg_start[1] = i
                    self.seg_end[3] = i
                    break

    def get_relevancy(self, x, y):
        i = self.word_idx.get(x)
        j = self.word_idx.get(y)
        if i is None or j is None:
            return []
        return self._ww[i, j]

    def _get_candidates(self, i, threshold=0, word_len=-1):
        assert(threshold >= 0)
        if word_len > 0:
            s, e = self.seg_start[word_len], self.seg_end[word_len]
        else:
            s, e = 0, len(self.word_itmes)
        w = self._ww[i][s:e].copy()
        idx = np.argsort(-w)
        w = -np.sort(-w)
        end_idx = np.where(w<=threshold)[0].min()
        return idx[:end_idx]
        
    def get_candidates(self, x, threshold=0, word_len=-1):
        i = self.word_idx.get(x)
        if i is None:
            return []
        idx = self._get_candidates(i, threshold, word_len)
        if word_len < 0:
            return [(self.word_itmes[j], self._ww[i, j]) for j in idx]
        else:
            return [(self.word_itmes[j+self.seg_start[word_len]], self._ww[i, j+self.seg_start[word_len]]) for j in idx]

    _instance = None
    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

if __name__ == '__main__':
    import sys
    p = Relevancy.getInstance()
    #ret = p.get_candidates('赤壁', 0.001)
    #print(ret)
    #print(len(ret))
    ret = p.get_candidates(sys.argv[1], 0.05)
    print(ret)
    print(len(ret))
