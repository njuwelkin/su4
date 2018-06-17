import numpy as np
from scipy import sparse 
import loader


class Relevancy(object):
    def __init__(self):
        # ww: N * N
        self._ww = np.load('./output/w_w.npy')

        self.words = loader.loadDictFromFreqFile('./res/word_dict.txt')
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

    def _get_candidates(self, i, word_len=2, threshold=1):
        assert(threshold >= 1)
        s, e = self.seg_start[word_len], self.seg_end[word_len]
        w = self._ww[i][s:e].copy()
        idx = np.argsort(-w)
        w = -np.sort(-w)
        end_idx = np.where(w==(threshold-1))[0].min()
        return idx[:end_idx]
        
    def get_candidates(self, x, word_len=2, threshold=1):
        i = self.word_idx.get(x)
        if i is None:
            return []
        idx = self._get_candidates(i, word_len, threshold)
        return [(self.word_itmes[j+self.seg_start[word_len]], self._ww[i, j+self.seg_start[word_len]]) for j in idx]

if __name__ == '__main__':
    p = Relevancy()
    print(p.get_relevancy('东风', '赤壁'))
    ret = p.get_candidates('赤壁')
    print(ret)
    print(len(ret))
    ret = p.get_candidates('赤壁', 3)
    print(ret)
    print(len(ret))
    ret = p.get_candidates('赤壁', 1, 1)
    print(ret)
    print(len(ret))
    #ret = p.get_candidates('东风')
    #print(ret)
    #print(len(ret))
