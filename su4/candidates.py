from relevancy import *
from datatype import Word
import queue
import random

class WordCandidate(object):
    pzy_dict = loader.loadKeyValues('./res/words_pzy.txt')
    def __init__(self, candidates):
        pzy_dict = self.__class__.pzy_dict
        self.pz_tables = {}
        self.yun_tables = {}
        self.pos_tables = {}
        self._cache = {}
        for k, v in pzy_dict.items():
            self._add_to_table(k, v)
        #print(self.pz_tables)

    def _add_to_table(self, k, v):
        pz = v[0]
        yuns = v[1:]
        if self.pz_tables.get(pz) is None:
            self.pz_tables[pz] = set()
        self.pz_tables[pz].add(k)
        for y in yuns:
            if self.yun_tables.get(y) is None:
                self.yun_tables[y] = set()
            self.yun_tables[y].add(k)

    def _match(self, pattern, instance):
        if len(pattern) != len(instance):
            return False
        for i in range(len(pattern)):
            if pattern[i] != '*' and instance[i] != '*' and pattern[i] != instance[i]:
                return False
        return True

    def _getCandidates(self, pz, yun=None):
        cache_key = "%s_%s" % (pz, yun)
        if self._cache.get(cache_key) is not None:
            return self._cache[cache_key]

        ret = set()
        for k in self.pz_tables.keys():
            if self._match(pz, k):
                ret |= self.pz_tables[k]
        if yun is not None:
            ret_yun = self.yun_tables[str(yun)]
            ret &= ret_yun

        self._cache[cache_key] = ret
        return ret

    def getRandomWord(self, pz, yun=None):
        ret = self._getCandidates(pz, yun)
        return list(ret)[random.randint(0, len(ret)-1)]

    

class WordGenerator(object):
    def __init__(self):
        self.r = Relevancy.getInstance()

    def _getCandidates(self, seeds, quantity):
        assert(type(seeds) is list)
        d = {}

        q = queue.Queue()
        for s in seeds:
            q.put((s, 1))
            d[s] = 1
            quantity -= 1

        while not q.empty():
            w, g = q.get()
            #print(w, g)
            candidates = self.r.get_candidates(w, 0.002*g)
            for c, r in candidates:
                if d.get(c) is None:
                    d[c] = 1
                    q.put((c, 10))
                    quantity -= 1
                    if quantity == 0:
                        return d.keys()

    def _init_ret(self):
        self.pz = {'0':[], '1':[], '*':[]}
        l = ['0', '1', '*']
        for i in l:
            for j in l:
                self.pz[i+j] = []
        return pz

    def getCandidates(self, seeds, quantity= 5000):
        candidates = self._getCandidates(seeds, quantity)
        return WordCandidate(candidates)


if __name__ == "__main__":
    import sys
    wg = WordGenerator()
    ret = wg.getCandidates(sys.argv[1:])
    #print("\n".join(ret))
    #print(len(ret))
    print(ret._getCandidates('00', 11))
