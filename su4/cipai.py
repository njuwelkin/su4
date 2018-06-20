import random

qpy1 = """
**/*1|a
*1/00/1|a
*1/*0/0*/1|a
*1/*0/*1|a
*1/*1/00|b
**/*1/*0|b
*1/*0/*1
**/*1/00|b
"""


qpy2 = """
**/*1|a
*1/00/1|a
*1/*0/0/*1|a
*1/*0/*1|a
*1/*1/00|b
**/*1/*0|b
*1/*0/*1
**/*1/00|b
"""
MAXYUN = 17
class CiPattern(object):
    def __init__(self, gelv, yun_dict={}):
        self.lines = []
        for line in gelv.split('\n'):
            line = line.strip()
            if len(line) == 0:
                continue
            l = line.split('|')
            yun = l[1] if len(l) == 2 else None
            pz = l[0].split('/')
            self.lines.append((pz, self._get_random_yun(yun_dict, yun)))

        self._gen_idx()

    def _get_random_yun(self, yun_dict, char_yun):
        if char_yun is None:
            return None
        if yun_dict.get(char_yun) is None:
            yun_dict[char_yun] = random.randint(0, MAXYUN)
        return yun_dict[char_yun]

    def _gen_idx(self):
        pz_idx = {}
        for i, line in enumerate(self.lines):
            for j, pz in enumerate(line[0]):
                if (j == len(line[0]) - 1) and (line[1] is not None):
                    continue
                if pz_idx.get(pz) is None:
                    pz_idx[pz] = []
                pz_idx[pz].append((i, j))
        self.pz_idx = pz_idx

    def pickRandomExchange(self, position):
        i, j = position
        lines = self.lines
        if (j == len(lines[i][0]) - 1) and (lines[i][1] is not None):
            return position
        pz = lines[i][0][j]
        l = self.pz_idx[pz]
        return l[random.randint(0, len(l) - 1)]

    def getPZYForPosition(self, postion):
        i, j = postion
        yun = None
        lines = self.lines
        if (j == len(lines[i][0]) - 1) and (lines[i][1] is not None):
            yun = lines[i][1]
        pz = lines[i][0][j]
        return pz, yun


if __name__ == '__main__':
    cp = CiPattern(qpy1)
    print(cp.lines)
    print(cp.pz_idx)
    print(cp.pickRandomExchange((0, 1)))
    print(cp.getPZYForPosition((0, 0)))
    print(cp.getPZYForPosition((0, 1)))





