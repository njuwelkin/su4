from su4_config import *
from individual import *
from candidates import *
from cipai import *

class Population(object):
    def __init__(self, size, topic):
        if size % 2 != 0:
            raise
        self.size = size

        cp = CiPattern(AllPatterns[0])
        wg = WordGenerator()
        candidates = wg.getCandidates([topic], 18000)

        self.indvs = []
        for i in range(size):
            indv = Individual(cp, candidates, topic)
            self.indvs.append(indv)

        self._fitness = [indv.fitness() for indv in self.indvs]
        self._updated = False

    def bestIndv(self):
        return max(self.indvs, key=lambda indv: indv.fitness())

    def bestFit(self):
        return max(self.all_fits())

    def worstFit(self):
        return min(self.all_fits())

    def all_fits(self):
        if self._updated:
            self._updated = False
            self._fitness = [indv.fitness() for indv in self.indvs]
        return self._fitness

    def update(self):
        self._updated = True

    def __getitem__(self, key):
        if key < 0 or key >= self.size:
            raise IndexError('Individual index({}) out of range'.format(key))
        return self.indvs[key]

    def __len__(self):
        return len(self.indvs)

if __name__ == '__main__':
    p = Population(QUANTITY, '周郎')
    print(p.bestIndv())
    print(p.bestIndv().fitness())
