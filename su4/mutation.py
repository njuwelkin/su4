import random
from su4_config import *
from individual import *
import numpy as np

class Mutation(object):
    def __init__(self, pm):
        self.setPm(pm)

    def setPm(self, pm):
        if pm <= 0.0 or pm > 1.0:
            raise ValueError('Invalid mutation probability')
        self.pm = pm

    def mutate(self, indv):
        '''
        Mutate the individual.
        '''
        do_mutation = True if random.random() <= self.pm else False

        if do_mutation:
            i = indv.f_cache.getMinFitLine()
            j = random.randint(0, indv.f_cache.count_lines[i]-1)
            indv.evolution(i, j)

        return indv

if __name__ == '__main__':
    from candidates import *
    from cipai import *
    cp = CiPattern(AllPatterns[0])
    wg = WordGenerator()
    candidates = wg.getCandidates(['周郎'], 8000)
    indv = Individual(cp, candidates, '周郎')
    print(indv.f_cache.getMinFitWord())
    print(indv.f_cache.getMinFitLine())
    print(indv.f_cache.fit_array)
    print(indv)

    m = Mutation(1.0)
    indv2 = m.mutate(indv)
    print(indv2.f_cache.fit_array)
    print(indv2)


