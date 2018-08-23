from copy import deepcopy
import random

class UniformCrossover(object):
    def __init__(self, pc, pe=0.2, pe2=0.5):
        if pc <= 0.0 or pc > 1.0:
            raise ValueError('Invalid crossover probability')
        self.pc = pc

        if pe <= 0.0 or pe > 1.0:
            raise ValueError('Invalid genome exchange probability')
        self.pe = pe

        if pe2 <= 0.0 or pe2 > 1.0:
            raise ValueError('Invalid genome exchange probability')
        self.pe2 = pe2

    def cross(self, father, mother):
        do_cross = True if random.random() <= self.pc else False

        if not do_cross:
            return father, mother

        # Chromsomes for two children.
        ml = father.f_cache.getMinFitLine()
        for i in range(len(father.f_cache.count_lines)):
            if father.f_cache.fit_lines[i] < mother.f_cache.fit_lines[i]:
                for j in range(father.f_cache.count_lines[i]):
                    tmp = father.lines[i][j]
                    father.update(i, j, mother.lines[i][j], False)
                    mother.update(i, j, tmp, False)
            else:
                p = self.pe2 if i == ml else self.pe
                for j in range(father.f_cache.count_lines[i]):
                    do_exchange = True if random.random() < p else False
                    if do_exchange:
                        tmp = father.lines[i][j]
                        father.update(i, j, mother.lines[i][j], False)
                        mother.update(i, j, tmp, False)
        father.f_cache.refresh()
        mother.f_cache.refresh()

        return father, mother


if __name__ == '__main__':
    from candidates import *
    from cipai import *
    from individual import *
    cp = CiPattern(AllPatterns[0])
    wg = WordGenerator()
    candidates = wg.getCandidates(['周郎'], 8000)
    indv = Individual(cp, candidates, '周郎')
    indv2 = Individual(cp, candidates, '周郎')
    print(indv)
    print(indv.f_cache.fit_array)
    print(indv2)
    print(indv.f_cache.fit_array)

    cross = UniformCrossover(0.8, 0.2)
    for i in cross.cross(indv, indv2):
        print(i)
        print(indv.f_cache.fit_array)
