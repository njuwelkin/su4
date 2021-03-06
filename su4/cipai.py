import random
from patterns import AllPatterns


MAXYUN = 17
class CiPattern(object):
    def __init__(self, pattern, yun_dict={}):
        gelv = pattern['gelv']
        gram = pattern['grammar']
        pzy = []
        for line in gelv.split('\n'):
            line = line.strip()
            if len(line) == 0:
                continue
            l = line.split('|')
            yun = l[1] if len(l) == 2 else None
            pz = l[0].split('/')
            pzy.append((pz, self._get_random_yun(yun_dict, yun)))

        grammar = []
        for line in gram.split('\n'):
            line = line.strip()
            if len(line) == 0:
                continue
            l = line.split()
            grammar.append(l)

        self.lines = []
        for i, line_p in enumerate(pzy):
            pos = grammar[i]
            pz = line_p[0]
            yun = [None] * (len(pz) - 1) + [line_p[1]]
            t = list(zip(pz, pos, yun))
            self.lines.append(t)

        #self._gen_idx()

    def _get_random_yun(self, yun_dict, char_yun):
        if char_yun is None:
            return None
        if yun_dict.get(char_yun) is None:
            yun_dict[char_yun] = random.randint(0, MAXYUN)
        return yun_dict[char_yun]


    def getPatternForPosition(self, postion):
        i, j = postion
        return self.lines[i][j]


if __name__ == '__main__':
    cp = CiPattern(AllPatterns[0])
    print(cp.lines)
    #print(cp.pz_idx)
    #print(cp.pickRandomExchange((0, 1)))
    print(cp.getPatternForPosition((0, 1)))
    #print(cp.getPZYForPosition((0, 1)))





