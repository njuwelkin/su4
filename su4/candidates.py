from relevancy import *
from datatype import Word
import queue
import random

class WordCandidate(object):
    pzy_dict = loader.loadKeyValues('./res/words_pzy.txt')
    pos_dict = loader.loadKeyValues('./res/words_pos.txt')
    def __init__(self, candidates):
        pzy_dict = self.__class__.pzy_dict
        pos_dict = self.__class__.pos_dict
        self.pz_tables = {}
        self.yun_tables = {}
        self.pos_tables = {}
        self._cache = {}
        for k in candidates:
            v = pzy_dict[k]
            self._add_to_pzy_table(k, v)
            v2 = pos_dict[k]
            self._add_to_pos_table(k, v2)
        #print(self.pz_tables)

    def _add_to_pzy_table(self, k, v):
        pz = v[0]
        yuns = v[1:]
        if self.pz_tables.get(pz) is None:
            self.pz_tables[pz] = set()
        self.pz_tables[pz].add(k)
        for y in yuns:
            if self.yun_tables.get(y) is None:
                self.yun_tables[y] = set()
            self.yun_tables[y].add(k)

    def _add_to_pos_table(self, k, v):
        if len(v) == 1:
            return
        pos = v[1:]
        for p in pos:
            if self.pos_tables.get(p) is None:
                self.pos_tables[p] = set()
            self.pos_tables[p].add(k)

    def _match_pz(self, pattern, instance):
        if len(pattern) != len(instance):
            return False
        for i in range(len(pattern)):
            if pattern[i] != '*' and instance[i] != '*' and pattern[i] != instance[i]:
                return False
        return True

    def _match_pos(self, req, candidate):
        d = {
            'n': ['ns', 'nr', 'sn', 'r'],
            'a': ['ae', 'af', 'an'],
            'ae': ['a'],
            'af': ['a', 'art'],
            's': ['ns', 'sn'],
            'w': ['wr', 'ws', 'wt'],
            'v': ['vi', 'vt', 'ae', 'a', 'v'],
            'vi': ['ae', 'a', 'v', 'v-n'],
            'vt': ['v'],
            'n-vi': ['n-a'],
            'df': ['dv', 'dft', 'p-v'],
            'wn': ['wr'],
        }
        reqs = req.strip().split('/')
        for r in reqs:
            if (r == candidate) or ((d.get(r) is not None) and (d[r].count(candidate) > 0)):
                return True
        return False

    def _getCandidates(self, pz, yun, pos):
        cache_key = "%s_%s_%s" % (pz, yun, pos)
        if self._cache.get(cache_key) is not None:
            return self._cache[cache_key]

        ret = set()
        for k in self.pz_tables.keys():
            if self._match_pz(pz, k):
                ret |= self.pz_tables[k]

        if yun is not None:
            ret_yun = self.yun_tables[str(yun)]
            ret &= ret_yun

        if pos is not None:
            ret_pos = set()
            for k in self.pos_tables.keys():
                if self._match_pos(pos, k):
                    ret_pos |= self.pos_tables[k]
            ret &= ret_pos

        self._cache[cache_key] = ret
        return ret

    def getRandomWord(self, pz, yun=None, pos=None):
        ret = self._getCandidates(pz, yun, pos)
        #if len(list(ret)) == 0:
        #    print(pz, yun, pos)
        res = list(ret)[random.randint(0, len(ret)-1)]
        #print(pz, yun, pos, len(ret), res)
        return res

    def getAllWords(self, pz, yun=None, pos=None):
        ret = self._getCandidates(pz, yun, pos)
        return list(ret)

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

    def getCandidates(self, seeds, quantity= 5000):
        candidates = self._getCandidates(seeds, quantity)
        #print(candidates)
        return WordCandidate(candidates)


if __name__ == "__main__":
    import sys
    wg = WordGenerator()
    ret = wg.getCandidates(sys.argv[1:], 500)
    #print("\n".join(ret))
    #print(len(ret))
    #print(ret.pos_tables.keys())
    #print(ret._getCandidates('00', None, None))
