from relevancy import *
from datatype import Word
import queue
import random

class WordCandidate(object):
    pzy_dict = loader.loadKeyValues('./res/words_pzy.txt')
    def __init__(self, candidates):
        pzy_dict = self.__class__.pzy_dict
        self.pz_tables = {'0':[], '1':[], '*':[]}
        l = ['0', '1', '*']
        for i in l:
            for j in l:
                self.pz_tables[i+j] = []
        for i in l:
            for j in l:
                for k in l:
                    self.pz_tables[i+j+k] = []
        for c in candidates:
            item = pzy_dict[c]
            yun = item[1:]
            self.pz_tables[item[0]].append((c, yun))
        #print(self.pz_tables)
        self._cache = {}

    def _match(self, pattern, instance):
        if len(pattern) != len(instance):
            return False
        for i in range(len(pattern)):
            if pattern[i] != '*' and instance[i] != '*' and pattern[i] != instance[i]:
                return False
        return True

    def _getCandidates(self, pz, yun):
        cache_key = "%s_%s" % (pz, yun)
        if self._cache.get(cache_key) is not None:
            return self._cache[cache_key]

        w_y = []
        for k in self.pz_tables.keys():
            if self._match(pz, k):
                w_y += self.pz_tables[k]
        if yun >= 0:
            ret = set()
            for i in w_y:
                if str(yun) in i[1]:
                    ret.add(i[0])
        else:
            ret = set([k for k, y in w_y])

        self._cache[cache_key] = ret
        return ret

    def getRandomWord(self, pz, yun):
        ret = self._getCandidates(pz, yun)
        return ret[random.randomint(0, len(ret))]

    

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

    def getCandidates(self, seeds, quantity= 6000):
        candidates = self._getCandidates(seeds, quantity)
        return WordCandidate(candidates)


if __name__ == "__main__":
    import sys
    wg = WordGenerator()
    ret = wg.getCandidates(sys.argv[1:])
    #print("\n".join(ret))
    #print(len(ret))
    print(ret._getCandidates('00', 11))
